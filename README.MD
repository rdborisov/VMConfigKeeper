Проект располагается по адресу:
https://nas.autonet.keenetic.link/


Изменения в Vagrantfile:
```
Vagrant.configure("2") do |config|

  config.vm.box = 'ubuntu/xenial64'
  ENV['VAGRANT_SERVER_URL'] = 'https://nas.autonet.keenetic.link/file/'
end
```
