package main

import (
	"fmt"
	"image/png"
	"os"
)

// open a png file
func openImage(fileName string) [][]byte {
	file, err := os.Open(fileName)
	if err != nil {
		fmt.Println(err)
		return nil
	}
	defer file.Close()

	// decode the png
	img, err := png.Decode(file)
	if err != nil {
		fmt.Println(err)
		return nil
	}

	// get the width and height of the image
	bounds := img.Bounds()
	width := bounds.Max.X
	height := bounds.Max.Y

	// create a 2D array of bytes
	var pixels [][]byte
	for i := 0; i < height; i++ {
		pixels = append(pixels, make([]byte, width))
	}

	// copy the pixels from the image to the 2D array
	for i := 0; i < height; i++ {
		for j := 0; j < width; j++ {
			r, _, _, _ := img.At(j, i).RGBA()
			pixels[i][j] = byte(r)
		}
	}

	return pixels
}

// loop over all the pixels
// for each pixel, print whether the pixel is black
// or white
func printPixels(pixels [][]byte) {
	for i := 0; i < len(pixels); i++ {
		for j := 0; j < len(pixels[i]); j++ {
			if pixels[i][j] == 0 {
				fmt.Print(" ")
			} else {
				fmt.Print(" ")
			}
		}
		fmt.Println()
	}
}

func main() {
	img := openImage("flag.png")
	// fmt.Println(img)
	printPixels(img)
}
