# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.provider :virtualbox do |vb|
		vb.customize [
			"modifyvm", :id,
			"--memory", 2048,
			"--ioapic", "on",
			"--vtxvpid", "on",    # enables tagged TLB (VPID) in host cpu
			"--pae", "on",       # extends addressable memory from 32 to 36 bit
			"--rtcuseutc", "on",  # enables RTC 'real time clock' to work in UTC
			"--nestedpaging", "on", # enables nested pages in host cpu
			"--largepages", "on",   # Enables use of Large Page in Hypervisor and less TLB use
			"--hwvirtex", "on",     # enable hw virtualisation
			#"--nictype2", "virtio"
		]
    end

	config.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'" #fixes:  default: stdin: is not a tty

    config.vm.box = "trusty64"
    config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
    config.vm.network "forwarded_port", guest: 8000, host: 8000
    


	# Provisioning
	config.vm.provision "shell" do |s|
		s.path = "src/vagrant/install.sh"
	end

	#starting celery and runserver in screens
	config.vm.provision "shell", run: "always" do |s|
		s.path = "src/vagrant/startup.sh"
	end
    
end