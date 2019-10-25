# gpg-decrypt-api
This is a REST API that decrypts a given GPG-encrypted message using a given passphrase. It's built with Flask RESTful, python-gnupg, Gunicorn, and Docker.

For now, this service expects the input message to be [symmetrically encrypted](https://www.tutonics.com/2012/11/gpg-encryption-guide-part-4-symmetric.html). Symmetric encryption uses the same key (passphrase) for both encryption and decryption. It needs only this passphrase to work, and does not involve setting up a public/private key pair.

## API Reference
The API currently only has one endpoint:

* **URL:** `/decryptMessage`
* **Method:** `POST`
* **URL Params:** None
* **Data Params:** A JSON object with the following keys:
    * `passphrase` -: used for message decryption
    * `message`: the GPG-encrypted message
* **Success Response:**
    * Code: 200
    * Content: JSON object with `DecryptedMessage` parameter
* **Error Response:**
    * Code: 400 (for bad input and bad requests)
    * Content: JSON object with `message` parameter that contains the given error message

## Running the Service
1. Build the Docker image:  
```
$ docker build -t IMAGE_NAME:IMAGE_TAG .
```
2. Run the container:  
```
$ docker run --rm -d -p SOME_PORT:5000 --name CONTAINER_NAME IMAGE_NAME:IMAGE_TAG
```

## Testing
To run the unit tests:
```
$ docker run --rm IMAGE_NAME:IMAGE_TAG run_tests.sh
```

To test the service with the `sample.json` file, make sure that the container is running (see Step 2 of preceding section) and use curl:
```
$ curl -vX POST http://localhost:SOME_PORT/decrypt \
  -d @sample.json \
  -H "Content-Type: application/json"
```

## Sources
* [python-gnupg - A Python wrapper for GnuPG](https://pythonhosted.org/python-gnupg/)
* [Python gnupg (GPG) example](https://www.saltycrane.com/blog/2011/10/python-gnupg-gpg-example/)
* [Encrypting and decrypting documents](https://www.gnupg.org/gph/en/manual/x110.html)
* [GPG Encryption Guide - Part 4 (Symmetric Encryption)](https://www.tutonics.com/2012/11/gpg-encryption-guide-part-4-symmetric.html)

## License
[MIT License](https://opensource.org/licenses/MIT)
