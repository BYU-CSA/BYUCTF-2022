package main

import (
	"bufio"
	"bytes"
	"crypto/aes"
	"crypto/cipher"
	"encoding/base64"
	"fmt"
	"math/rand"
	"os"
	"time"
)

func readFromOutput() ([]byte, []byte, error) {
	output_file, _ := os.Open("output.txt")
	defer output_file.Close()
	scanner := bufio.NewScanner(output_file)
	scanner.Scan()
	nonce, _ := base64.StdEncoding.DecodeString(scanner.Text()[len("Nonce: "):])
	scanner.Scan()
	ciphertext, _ := base64.StdEncoding.DecodeString(scanner.Text()[len("Ciphertext: "):])
	return nonce, ciphertext, nil
}

func main() {
	real_nonce, ciphertext, _ := readFromOutput()
	var key []byte
	var nonce []byte

	now := time.Now().Unix()
	for seed := now; bytes.Compare(nonce, real_nonce) != 0; seed-- {
		rand.Seed(seed)
		key = make([]byte, 16)
		rand.Read(key)

		nonce = make([]byte, 12)
		rand.Read(nonce)
	}

	block, _ := aes.NewCipher(key)
	aesgcm, _ := cipher.NewGCM(block)
	plaintext, _ := aesgcm.Open(nil, real_nonce, ciphertext, nil)

	fmt.Printf("Plaintext: %s\n", string(plaintext))
}
