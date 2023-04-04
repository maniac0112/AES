This is a python implementation of AES-128 algorithm.
We convert an image into ciphertext using AES128 algorithm. We can also recover the orignal image using another decryption algorithm.

The different block elements - 
mix columns, shift rows, byte substitution, adding round key, the key expansion algorithm and their inverse 
are implemented in their own file. 

The main file has a function that takes in input the image name (with extension) in this directory.
It converts the image to a binary string of Height *Width* 3 * 8 size and convert it to ciphertext and saves
it in this directory. It then decrypts the same ciphertext using the symmetric key for aes encryption. 
It then converts the decrypted string back to image, and saves it as decrypted.jpg 
