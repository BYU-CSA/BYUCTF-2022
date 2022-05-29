# C-Spring Write-up
The challenge uses AES GCM, a mode of AES. The key and nonce were generated insecurely, however, as consecutive random generations from an insecurely-seeded random number generator.

Given the nonce, we can determine the key by finding the seed that generated the nonce. We find the seed by simply taking the current Unix time (in seconds), and decrementing that value until it gives us the proper nonce (after generating a key), and thus we have the right key. 

We then use the key and nonce on the ciphertext to decrypt.

The whole guessing takes about a second per day of guesses. (i.e. if the output were made 1 week ago, the solution would be found in about 7 seconds.) Thus we should have no problem making the output now and using that as the final version of the challenge.

---------------

**Note** - a change was made here by Justin before the public CTF. Instead of giving them the Go file, I compiled it and gave them the binary and marked it as a hard challenge. They're welcome :)

**Flag** - `byuctf{dont_seed_with_time_in_secure_contexts_WiOuYiaZ}`