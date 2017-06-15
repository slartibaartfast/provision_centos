# Provision Vagrant with Ansible
This is a playbook which performs some installation and configuration tasks for running a python application on a centos vm.
Change the certificates and application for practical uses.

- Lets Nginx accept requests on ports 80 and 443
- Permanently redirects all `http` requests to their `https` equivalent
- Uses the provided `files/self-signed.crt` and `files/self-signed.key` for your SSL configuration
- Lets Nginx proxy requests to the upstream application
- Passes headers `X-Forwarded-For` and `X-Real-IP` to the upstream application with appropriate values

# Some of the tasks
- Install nginx and runit
- Copy `config/nginx.conf`, `files/self-signed.key` and `files/self-signed.crt` to appropriate locations on the destination box
- Ensure appropriate file permissions are set for each of the three files mentioned above
- Copy and unzips/untars the contents of application.zip to `/opt/application/` on the destination box
- Install and configure the application's `run` script as a runit service
- Start nginx using the configuration you completed and copied to the box

### Testing

Test playbook by running `./provision.sh`.

A working configuration will render:

```
Pass: status code is 200
Pass: X-Forwarded-For is present and not 'None'
Pass: X-Real-IP is present and not 'None'
Pass: found "It's easier to ask forgiveness than it is to get permission." in response
```
