# Convert a python http webapp to a https webapp

The project is to convert a python http webapp to https webapp, then the certificate can be secured by a [confidential-containers](https://github.com/confidential-containers). So that the web browser can identify any malicious webapp.

## Learn point:

- [ ] Understand the browser and server data flow
- [ ] Understand the difference between http and https
- [ ] Understand encryption, signature and certificate, refer [document](https://github.com/huoqifeng/document/blob/master/security/encryption-signature-cert.md)
- [ ] Understand Linux operation system
- [ ] Understand virtual machine and container
- [ ] Understand container image and container
- [ ] Understand common docker command, like pull, run, exec etc
- [ ] Learn how to pull an container image from registry via docker
- [ ] Learn how to run a container via docker
- [ ] Run the python webapp via http and access it in browser

## Add https support (this is the goal of this project)
- [ ] Generate a self-generated certificate
- [ ] Add the certificate in the webapp
- [ ] Build a new container image
- [ ] Push the image to registry, like dockerhub
- [ ] Run the new webapp and access it via https
