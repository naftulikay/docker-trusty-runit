# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'etc'
require 'shellwords'

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "phusion/ubuntu-14.04-amd64"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network "private_network", type: "dhcp"

  # Save Valuable Disk Space!
  config.vm.provider "virtualbox" do |v|
    v.cpus = [Etc.nprocessors, 2].min
    v.linked_clone = true if Vagrant::VERSION =~ /^1.8/
  end

  # Provision using an internal Ansible on the guest
  config.vm.provision "ansible_local" do |ansible|
    # allow passing ansible args from environment variable
    ansible.raw_arguments = Shellwords::shellwords(ENV.fetch("ANSIBLE_ARGS", ""))
    ansible.provisioning_path = "/vagrant/ansible/"
    ansible.playbook = "vagrant-playbook.yml"
  end
end
