require "yast/rake"

Yast::Tasks.configuration do |conf|
  #lets ignore license check for now
  conf.skip_license_check << /.*/
end

Packaging.configuration do |conf|
  conf.obs_api = "https://api.suse.de"
  conf.obs_project = "Devel:YaST:Head"
  conf.obs_target = "SLE-12"
  conf.obs_sr_project = "SUSE:SLE-12:GA"
end

# no tarball is needed for package build
Rake::Task["tarball"].clear_actions

