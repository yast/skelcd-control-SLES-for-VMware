skelcd-control-SLES-for-VMware
==============================

This repository contains sources for building the installation control file
(`control.xml`) for the SUSE Linux Enterprise Server for VMware product.


How the package works?
----------------------

The package takes the original `control.xml` file from `skelcd-control-SLES`
package and applies a [XSL transformation](package/control.SLES-for-VMware.xsl).

*Note: Currently there is just the identity XSL pattern - it copies all input tags to the output. The result is the
original SLES control file for now.*


How to change it?
-----------------

See [the contributing documentation](CONTRIBUTING.md) for details
(but it's a generic file for all Yast packages, some parts might not make sense
for this package). See also [the Github fork workflow](https://help.github.com/articles/fork-a-repo)


How to build it or submit?
--------------------------

The package is built (and possibly submitted) automatically by [the internal Jenkins CI node]
(http://river.suse.de/view/YaST/job/yast-skelcd-control-SLES-for-VMware-master/) after each Git commit.


- When the build succeeds the package is submitted to IBS [Devel:YaST:Head project]
(https://build.suse.de/package/show/Devel:YaST:Head/skelcd-control-SLES-for-VMware)

- If the `Version` tag in [the spec](package/skelcd-control-SLES-for-VMware.spec) file
is changed a submit request to [SUSE:SLE-12:GA](https://build.suse.de/project/show/SUSE:SLE-12:GA)
is sent automatically by the Jenkins job.
