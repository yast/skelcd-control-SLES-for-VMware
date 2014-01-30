#
# spec file for package skelcd-control-SLES-for-VMware
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


######################################################################
#
# IMPORTANT: Please do not change the control file or this spec file
#   in build service directly, use
#   https://github.com/yast/skelcd-control-SLES-for-VMware repository
#
#   See https://github.com/yast/skelcd-control-SLES-for-VMware/blob/master/CONTRIBUTING.md
#   for more details.
#
######################################################################

Name:           skelcd-control-SLES-for-VMware

# xsltproc for converting SLES control file to SLES-for-VMware
BuildRequires:  libxslt-tools
# xmllint (for validation)
BuildRequires:  libxml2-tools
# RNG validation schema
BuildRequires:  yast2-installation-control

# original SLES control file
BuildRequires:  skelcd-control-SLES
# ignore dependencies of skelcd-control-SLES, they are only needed to install
# Yast packages into inst-sys, they are not needed for control file conversion
#!BuildIgnore: yast2-registration yast2-theme-SLE autoyast2-installation yast2-add-on
#!BuildIgnore: yast2-buildtools yast2-devtools yast2-fcoe-client yast2-iscsi-client
#!BuildIgnore: yast2-kdump yast2-multipath yast2-network yast2-nfs-client yast2-ntp-client
#!BuildIgnore: yast2-proxy yast2-services-manager yast2-slp yast2-trans-allpacks
#!BuildIgnore: yast2-trans-stats yast2-tune yast2-update yast2-users yast2-x11
#!BuildIgnore: yast2-reipl yast2-vm

Url:            https://github.com/yast/skelcd-control-SLES-for-VMware
AutoReqProv:    off
Version:        12.0.0
Release:        0
Summary:        SLES-for-VMware control file needed for installation
License:        MIT
Group:          Metapackages
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        control.SLES-for-VMware.xsl

%description
This package contains control file for SLES-for-VMware product.

%prep

%build
# transform ("patch") the original SLES control file
xsltproc %{SOURCE0} /CD1/control.xml > control.xml

%check
#
# Verify syntax
#
xmllint --noout --relaxng /usr/share/YaST2/control/control.rng control.xml

%install
#
# Add control file 
#
mkdir -p $RPM_BUILD_ROOT/CD1
install -m 644 control.xml $RPM_BUILD_ROOT/CD1/


%files
%defattr(644,root,root,755)
/CD1

%changelog
