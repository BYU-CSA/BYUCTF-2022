# Alpine 1 Writeup
Once the attacker got in to mjohnson's account, they created an SSH key and put the private key in the `authorized_keys` files so that a password wasn't needed - they would be authenticated through the key instead! This can be seen inside of the `.bash_history` file.

**Flag** - `byuctf{/home/mjohnson/.ssh/authorized_keys}`