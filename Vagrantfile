# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get -y install python ansible
  SHELL

  config.vm.define "backend", primary: true do |backend|
    backend.vm.box = "ubuntu/xenial64"
    backend.vm.network "private_network", ip: "10.20.30.40"
    backend.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
    end
    # Ansible provisioning
    backend.vm.provision :ansible do |ansible|
      ansible.playbook = "provisioning/backend.yml"
      ansible.galaxy_role_file = "provisioning/requirements.yml"
      ansible.galaxy_roles_path = "provisioning/galaxy_roles/"
    end
  end

  # config.vm.define "db" do |db|
  #   db.vm.box = "ubuntu/xenial64"
  #   db.vm.network "private_network", ip: "10.20.30.41"
  #   db.vm.provider "virtualbox" do |vb|
  #     vb.memory = "512"
  #   end
  #   db.vm.provision :ansible do |ansible|
  #     ansible.playbook = "provisioning/db_playbook.yml"
  #   end
  # end

  # config.vm.define "api" do |api|
  #   api.vm.box = "ubuntu/xenial64"
  #   api.vm.network "private_network", ip: "10.20.30.42"
  #   api.vm.provider "virtualbox" do |vb|
  #     vb.memory = "1024"
  #   end
  #   api.vm.provision :ansible do |ansible|
  #     ansible.playbook = "provisioning/backend_playbook.yml"
  #   end
  # end

end
