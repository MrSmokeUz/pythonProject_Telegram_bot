 let isEncrypting = true; // Флаг текущего действия (шифрование или дешифрование)
 let currentMethod = 'caesar'; // Текущий метод шифрования

        // Основная функция шифрования/дешифрования для Caesar Cipher
        function caesarCipher(text, shift, action) {
            const shiftValue = action === 'decrypt' ? -shift : shift;
            return text.split('').map(char => {
                if (/[a-zA-Z]/.test(char)) {
                    const base = char.charCodeAt(0) >= 97 ? 97 : 65;
                    return String.fromCharCode(
                        ((char.charCodeAt(0) - base + shiftValue + 26) % 26) + base
                    );
                }
                return char;
            }).join('');
        }

        // Заглушки для других методов шифрования
        function rsaEncryptDecrypt(text, action) {
            return action === 'encrypt' ? `RSA Encrypted: ${text}` : `RSA Decrypted: ${text}`;
        }

        function aesEncryptDecrypt(text, action) {
            return action === 'encrypt' ? `AES Encrypted: ${text}` : `AES Decrypted: ${text}`;
        }

        function blowfishEncryptDecrypt(text, action) {
            return action === 'encrypt' ? `Blowfish Encrypted: ${text}` : `Blowfish Decrypted: ${text}`;
        }

        // Переключение между шифрованием и дешифрованием
        function toggleAction() {
            isEncrypting = !isEncrypting;
            const actionText = isEncrypting ? 'Encrypt' : 'Decrypt';

            document.getElementById('action-btn').innerText = actionText;
            document.getElementById('toggle-action-btn').innerText = isEncrypting ? 'Switch to Decrypt' : 'Switch to Encrypt';

            document.getElementById('input-description').innerText = isEncrypting ? 'Encrypting' : 'Decrypting';
            document.getElementById('output-description').innerText = isEncrypting ? 'Decrypting' : 'Encrypting';

            const inputField = document.getElementById('input-text');
            const outputField = document.getElementById('output-text');

            const temp = inputField.value;
            inputField.value = outputField.value;
            outputField.value = temp;
        }

        // Изменение метода шифрования
        function changeMethod() {
            currentMethod = document.getElementById('encryption-method').value;
            const keyField = document.getElementById('key');

            if (currentMethod === 'caesar') {
                keyField.style.display = 'block';
                keyField.placeholder = 'Enter shift key (e.g., 3)';
            } else {
                keyField.style.display = 'none';
            }
        }

        // Выполнение текущего действия
        function performAction() {
            const text = document.getElementById('input-text').value;
            const key = parseInt(document.getElementById('key').value, 10);

            let result;

            switch (currentMethod) {
                case 'caesar':
                    if (isNaN(key)) {
                        alert('Please enter a valid numeric key.');
                        return;
                    }
                    const action = isEncrypting ? 'encrypt' : 'decrypt';
                    result = caesarCipher(text, key, action);
                    break;
                case 'rsa':
                    result = rsaEncryptDecrypt(text, isEncrypting ? 'encrypt' : 'decrypt');
                    break;
                case 'aes':
                    result = aesEncryptDecrypt(text, isEncrypting ? 'encrypt' : 'decrypt');
                    break;
                case 'blowfish':
                    result = blowfishEncryptDecrypt(text, isEncrypting ? 'encrypt' : 'decrypt');
                    break;
                default:
                    alert('Unsupported encryption method.');
                    return;
            }

            document.getElementById('output-text').value = result;
        }