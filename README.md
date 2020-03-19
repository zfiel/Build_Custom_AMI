# Build_Custom_AMI
## Présentation
Le Build_Custom_AMI utilise Packer en utilisant Ansible en tant que "provisioner" pour déployer une image sur AWS (AMI).

Contrairement au Build_AMI classique, Ansible embarque ici différents rôles (mis en place grâce à Ansible Galaxy). Au sein du pipeline Jenkins, il est possible de choisir un unique role à déployer via ansible sur l'instance.

La liste des rôles proposés est la suivante : 
- website
- fail2ban
- mongodb
- utils
- nginx
