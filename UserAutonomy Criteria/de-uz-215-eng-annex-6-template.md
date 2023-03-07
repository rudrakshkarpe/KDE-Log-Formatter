# Annex 6: Product information

## 3.1.3.3: Continuity of the software product

### Requirements

* Security updates must be provided free of charge
* Security updates for the labelled product for at least 5 years after the end of sale
* The user must be given the option of whether to install only security updates or also other (e.g., functional) updates.

### Product information in which fullfilement of requirements is documented

<SOFTWARE NAME> has a history of continuous incremental updates as a free and open source product for <NUMBER> years starting in <YEAR>. See [full list of release announcements](<LINK>) *IF MISSING, ADD THIS INFORMATION TO DOCS*. All updates always have been and always will be released free of charge.

*WHEN APPLICABLE, OR SIMILAR* <SOFTWARE NAME> is released as part of the collection of KDE applications the KDE project releases on a [4 month release schedule](https://community.kde.org/Schedules). From April 2021 on this set is called "KDE Gear". In the years before it was mainly known as "KDE Applications". This release schedule is maintained by the KDE community and supported by KDE e.V. The community is committed to doing this indefinitely.

As the source code is released as open source, it always will be possible for others to pick up <SOFTWARE NAME> releases and continue them. <SOFTWARE NAME> is shipped by many Linux distributions which give a variety of different support levels. Some distributions offer multi-year plans. See also the [packaging status](<LINK>).

The openness of the code, the proven sustainable community and organization behind it, which by its nature is more independent of economic challenges than commercial companies, and the diversity of third parties vendors which distribute <SOFTWARE NAME> in various forms guarantee <SOFTWARE NAME>'s continuity as a software product over a long period of time, going way beyond a 5 year perspective.

The continuous incremental releases make sure users reliably get a working product with latest security updates. This includes the changes necessary to adapt to releases of dependencies which fix security related problems. Functional changes are incremental and it would not serve users to separate them from pure security updates becuase users would be blocked from critical fixes and security updates of dependencies.

Because of the code being released as free and open source code users also always have the option to maintain their own branch of <SOFTWARE NAME>, backport the fixes they need or add their own ones. This could also be done by one of the many distributors who ship versions of <SOFTWARE NAME> for the users who are not capable or willing to do it themselves.

In any case, continuity is guaranteed in principle forever by the chosen free and open source license.

## 3.1.3.4: Uninstallability

### Requirement

* Residue-free uninstallability of the software

### Product information in which fullfilement of requirements is documented

<SOFTWARE NAME> can be uninstalled without leaving residues on the system. The exact procedure depends on how it has been installed.

When installing from sources, cmake produces a list of files to delete which can be done with a simple shell script. Users who install from sources know how to do that.

When installing binary packages, the instructions of the package provider apply. With Linux distributions there usually is a command line tool which has some kind of uninstall command. They also usually offer graphical applications to uninstall packages.

For example the uninstall instructions for the <EXAMPLE PACKAGE MANAGER>, which is linked on the <SOFTWARE NAME> Website on the [download page](<LINK>), are in the [<EXAMPLE PACKAGE MANAGER> website](<LINK>) *IF MISSING, ADD THIS INFORMATION TO DOCS*.

The data <SOFTWARE NAME> handles is completely separate from the program. It is under full control of the user. An uninstallation will not touch any user-generated data.

## 3.1.3.5: Offline capability

### Requirement

* The functionality and availability of the software must not be negatively influenced by external factors, such as the availability of a licence server.

### Product information in which fullfilement of requirements is documented

<SOFTWARE NAME> is fully capable of offline usage. No network connections are required for any operations other than when the user explicitly specifies a document or similar to be retrieved over the network. Because <SOFTWARE NAME> does not require network connections in any way, there is no specific documentation needed.

## 3.1.3.6: Modularity

### Requirements

* Information on how individual modules of the software product can be deactivated during the installation process.
* Information on the extent to which individual modules of the software product (especially those that do not belong to the functions of the software product such as tracking, etc.) can be deactivated during the use of the software product.

### Product information in which fullfilement of requirements is documented

<SOFTWARE NAME> is a single purpose application for <SHORT DESCRIPTION, E.G., TEXT EDITING>. It is mostly used as a modular part of a desktop, often the KDE Plasma desktop, but also desktops on other platforms. It does not have extra modules which are unrelated to its core functionality, such as tracking or cloud integration, etc.

When installing from source it can be configured for the platform it is intended to run on and optional functionality is only built if the corresponding dependencies such as <OPTIONAL FUNCTIONALITY> are available. Technical details are made available in the [build control file](<LINK>/CMakeLists.txt).

When <SOFTWARE NAME> is installed from packages built by Linux distributions or other packagers, they usually are built in a modular way, so that for example translations of the user interface or the manuals can be installed separately, in the configuartion chosen by the user. Example: [<MODULARITY DESCRIPTION>](<LINK>).

## 3.1.3.7: Freedom from advertising

### Requirement

* Information on displaying advertising that will result in the transmission of data from the client to the server and vice versa

### Product information in which fullfilement of requirements is documented

Per compliance verification, see Annex 1.

## 3.1.3.8: Documentation of the software product, licence conditions and terms of use

### Requirement

Information about the software product both publicly and also in combination with the product itself:

a) Description of the processes for installing and uninstalling the software
b) Description of the data import and export processes
c) Information on reducing the use of resources
d) Information on the licensing terms and terms of use to enable, where relevant, the legally compliant further development of the software product
e) Information on software support
f) Information on the handling of data, in the sense of existing data protection laws
g) Information on data security, data collection and data transmission

### Product information in which fullfilement of requirements is documented

a) Description of the processes for installing and uninstalling the software

<SOFTWARE NAME> can be installed in several ways, depending on preferences of users and which platforms they use. There is a detailed overview of installation options: https://<SOFTWARE NAME>.kde.org/download *IF MISSING, ADD THIS INFORMATION TO DOCS*. Specific instructions for installing and uninstalling are part of the instructions and documentation of the general platforms used to handle the specific <SOFTWARE NAME> packages chosen by users. <SOFTWARE NAME> gives users full control here by enabling them to chose their preferred installation mechanism. Generic documentation which is applicable to <SOFTWARE NAME> is available as [tutorial for installing KDE applications](https://userbase.kde.org/Tutorials/Install_KDE_software) on [KDE UserBase](https://userbase.kde.org)

b) Description of the data import and export processes

As a <SHORT DESCRIPTION> <SOFTWARE NAME> is mostly about <WHAT SOFTWARE DOES>. A detailed list of formats and specific capabilites supported for each of them is documented: https://<SOFTWARE NAME>.kde.org/formats/ *IF MISSING, ADD THIS INFORMATION TO DOCS*. In the vast majority of use cases data is not changed or created, so no export is necessary. In the few cases where data is changed (e.g., <EXAMPLE OF DATA BEING CHANGED, E.G., ANNOTATION>) it uses the standard functionality for saving document data which is well known by users.

c) Information on reducing the use of resources

<SOFTWARE NAME> is designed to make effective use of resources. It focuses on the core functionality of viewing documents and does not include any functionality which would consume resources going beyond what is necessary to serve this core purpose. Information how some configuration parameters can affect performance and resource usage are documented in the manual: https://docs.kde.org/<SOFTWARE NAME>/configperformance.html *IF MISSING, ADD THIS INFORMATION TO DOCS*.

d) Information on the licensing terms and terms of use to enable, where relevant, the legally compliant further development of the software product

<SOFTWARE NAME> is Free Software and released under the <LICENSE NAME, E.G., GNU Public License> which allows unlimited use and modifications and distribution of changes as long as this is done under the <LICENSE NAME, E.G:, GPL> as well. This is stated in the "Free Software" section on the web site: https://<SOFTWARE NAME>.kde.org/. The source code for <SOFTWARE NAME> is publically available: https://invent.kde.org/<SOFTWARE NAME>. The full text of the license is part of the code and is required to be part of any distribution of <SOFTWARE NAME>: https://invent.kde.org/<SOFTWARE NAME>/-/blob/master/COPYING. The license is also stated in the <SOFTWARE NAME> manual: https://docs.kde.org/<SOFTWARE NAME>/credits.html *IF MISSING, ADD THIS INFORMATION TO DOCS*.

e) Information on software support

<SOFTWARE NAME> is supported by the [KDE community](https://kde.org). Specific forums and points of contacts for <SOFTWARE NAME> are available and documented: https://<SOFTWARE NAME>.kde.org/contact/.

f) Information on the handling of data, in the sense of existing data protection laws

There is no collection of personal data. <SOFTWARE NAME> is fully compliant with existing data protection laws. The full privacy policy can be found here: https://kde.org/privacypolicy-apps/.

g) Information on data security, data collection, and data transmission

Full documentation of data handling can be found in the KDE privacy policy: https://kde.org/privacypolicy-apps/. It also references the KDE Telemetry policy, which describes how telemetry data is collected in a way which fully protects user's privacy: https://community.kde.org/Policies/Telemetry_Policy.

<SOFTWARE NAME> does not collect personal data and specifically does not transmit any data to other systems or parties. There are no ads, no user tracking. Users are always in full control of what they do with their data.

## 3.2.1: Requirements for the further development and update of the product

### Requirement

If the product is changed (e.g., through updates), it must be ensure that the software product still complies with all of the criteria.

### Product information in which fullfilement of requirements is documented

Future updates are not expected to change the product in a way which significantly affects any of the requirements.
