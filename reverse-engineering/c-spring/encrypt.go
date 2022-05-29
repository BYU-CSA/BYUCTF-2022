package main

import (
	"bufio"
	"crypto/aes"
	"crypto/cipher"
	"encoding/base64"
	"fmt"
	"math/rand"
	"os"
	"time"
)

func readFlag() ([]byte, error) {
	flag_file, err := os.Open("flag.txt")
	if err != nil {
		return nil, err
	}
	defer flag_file.Close()
	scanner := bufio.NewScanner(flag_file)
	scanner.Scan()
	flag := scanner.Bytes()
	return flag, nil
}

func main() {
	seed := time.Now().Unix()
	rand.Seed(seed)

	key := make([]byte, 16)
	rand.Read(key)

	nonce := make([]byte, 12)
	rand.Read(nonce)

	message, err := readFlag()

	block, err := aes.NewCipher(key)
	if err != nil {
		panic(err.Error())
	}

	aesgcm, err := cipher.NewGCM(block)
	if err != nil {
		panic(err.Error())
	}

	ciphertext := aesgcm.Seal(nil, nonce, message, nil)
	fmt.Println("Nonce:", base64.StdEncoding.EncodeToString(nonce))
	fmt.Println("Ciphertext:", base64.StdEncoding.EncodeToString(ciphertext))
}
