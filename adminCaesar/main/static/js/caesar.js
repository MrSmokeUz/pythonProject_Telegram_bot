
fetch(`templates/main/${method}.html`)

   function toggleAction() {
            currentAction = currentAction === "encrypt" ? "decrypt" : "encrypt";
            document.getElementById("action-btn").textContent = currentAction.charAt(0).toUpperCase() + currentAction.slice(1);
            document.getElementById("input-description").textContent = currentAction === "encrypt" ? "Encrypting" : "Decrypting";
            document.getElementById("output-description").textContent = currentAction === "encrypt" ? "Decrypting" : "Encrypting";
        }

        function changeMethod() {
            const method = document.getElementById("encryption-method").value;
            document.getElementById("key").placeholder = getKeyPlaceholder(method);
        }

        function getKeyPlaceholder(method) {
            switch (method) {
                case "caesar":
                    return "Enter shift key (e.g., 3)";
                case "aes":
                case "blowfish":
                case "des":
                case "tripledes":
                    return "Enter secret key";
                case "vigenere":
                    return "Enter keyword";
                case "otp":
                    return "Enter one-time pad key";
                default:
                    return "Enter key (if needed)";
            }
        }

        function performAction() {
            const method = document.getElementById("encryption-method").value;
            const text = document.getElementById("input-text").value;
            const key = document.getElementById("key").value;

            let result;
            if (currentAction === "encrypt") {
                result = encrypt(method, text, key);
            } else {
                result = decrypt(method, text, key);
            }

            document.getElementById("output-text").value = result;
        }

        function encrypt(method, text, key) {
            switch (method) {
                case "caesar":
                    return caesarCipher(text, parseInt(key));
                case "aes":
                    return CryptoJS.AES.encrypt(text, key).toString();
                case "rsa":
                    const rsaEncrypt = new JSEncrypt();
                    rsaEncrypt.setPublicKey(key);
                    return rsaEncrypt.encrypt(text);
                case "vigenere":
                    return vigenereCipher(text, key);
                case "md5":
                    return CryptoJS.MD5(text).toString();
                case "sha256":
                    return CryptoJS.SHA256(text).toString();
                case "blowfish":
                    return CryptoJS.Blowfish.encrypt(text, key).toString();
                case "des":
                    return CryptoJS.DES.encrypt(text, key).toString();
                case "tripledes":
                    return CryptoJS.TripleDES.encrypt(text, key).toString();
                case "otp":
                    return oneTimePadEncrypt(text, key);
                default:
                    return "Unsupported encryption method";
            }
        }

        function decrypt(method, text, key) {
            switch (method) {
                case "caesar":
                    return caesarCipher(text, parseInt(key), true);
                case "aes":
                    const aesBytes = CryptoJS.AES.decrypt(text, key);
                    return aesBytes.toString(CryptoJS.enc.Utf8);
                case "rsa":
                    const rsaDecrypt = new JSEncrypt();
                    rsaDecrypt.setPrivateKey(key);
                    return rsaDecrypt.decrypt(text);
                case "vigenere":
                    return vigenereCipher(text, key, true);
                case "blowfish":
                    const blowfishBytes = CryptoJS.Blowfish.decrypt(text, key);
                    return blowfishBytes.toString(CryptoJS.enc.Utf8);
                case "des":
                    const desBytes = CryptoJS.DES.decrypt(text, key);
                    return desBytes.toString(CryptoJS.enc.Utf8);
                case "tripledes":
                    const tripleDesBytes = CryptoJS.TripleDES.decrypt(text, key);
                    return tripleDesBytes.toString(CryptoJS.enc.Utf8);
                case "otp":
                    return oneTimePadDecrypt(text, key);
                default:
                    return "Unsupported decryption method";
            }
        }

        function caesarCipher(str, shift, decrypt = false) {
            if (decrypt) shift = -shift;
            return str.replace(/[a-z]/gi, (char) => {
                const start = char >= 'a' ? 97 : 65;
                return String.fromCharCode(((char.charCodeAt(0) - start + shift + 26) % 26) + start);
            });
        }

        function vigenereCipher(str, key, decrypt = false) {
            const keyLength = key.length;
            const keyCodes = key.toUpperCase().split('').map(c => c.charCodeAt(0) - 65);
            return str.replace(/[a-z]/gi, (char, i) => {
                const start = char >= 'a' ? 97 : 65;
                const shift = keyCodes[i % keyLength] * (decrypt ? -1 : 1);
                return String.fromCharCode(((char.charCodeAt(0) - start + shift + 26) % 26) + start);
            });
        }

        function oneTimePadEncrypt(text, key) {
            if (key.length < text.length) return "Key must be at least as long as text";
            return text.split('').map((char, i) => String.fromCharCode(char.charCodeAt(0) ^ key.charCodeAt(i))).join('');
        }

        function oneTimePadDecrypt(text, key) {
            return oneTimePadEncrypt(text, key); // XOR is symmetric
        }
          function loadEncryptionPage() {
            const method = document.getElementById("encryption-method").value;
            const container = document.getElementById("encryption-container");

            fetch(`${method}.html`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`Failed to load ${method}.html`);
                    }
                    return response.text();
                })
                .then(html => {
                    container.innerHTML = html;
                })
                .catch(error => {
                    container.innerHTML = `<p>Error: ${error.message}</p>`;
                });
        }

        // Загрузка страницы по умолчанию
        window.onload = () => {
            loadEncryptionPage();
        };

