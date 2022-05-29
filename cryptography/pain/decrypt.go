package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
)

func readEncrypted() (string, error) {
	encrypted_file, err := os.Open("encrypted.txt")
	if err != nil {
		return "", err
	}
	defer encrypted_file.Close()
	scanner := bufio.NewScanner(encrypted_file)
	scanner.Scan()
	flag := scanner.Text()
	return flag, nil
}

func decode(encrypted string) string {
	codex_file, err := os.Open("CROSSWD.TXT")
	if err != nil {
		return ""
	}
	defer codex_file.Close()
	all_letters := []byte{}
	for _, word := range strings.Fields(encrypted) {
		decoded := decode_one(word, codex_file)
		all_letters = append(all_letters, byte(decoded>>8))
		all_letters = append(all_letters, byte(decoded&0xff))
	}
	return string(all_letters)
}

func decode_one(word string, codex_file *os.File) uint16 {
	codex_file.Seek(0, io.SeekStart)
	scanner := bufio.NewScanner(codex_file)
	for i := uint16(0); ; i++ {
		scanner.Scan()
		if scanner.Text() == word {
			return i + 1
		}
	}
}

func main() {
	encrypted, err := readEncrypted()
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(decode(encrypted))
}
