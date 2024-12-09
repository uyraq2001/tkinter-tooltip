%define _unpackaged_files_terminate_build 1
%define pypi_name tkinter-tooltip
%define mod_name python3-module-%pypi_name
%define short_name tktooltip

%def_without check

Name: %mod_name
Version: 3.1.2
Release: alt1
Summary: This is a simple yet fully customisable tooltip/pop-up implementation for tkinter widgets.
License: MIT
Group: Development/Tools
Url: https://pypi.org/project/%pypi_name
Vcs: https://github.com/gnikit/%pypi_name
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

# mapping of PyPI name to distro name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

BuildRequires(pre): rpm-build-pyproject

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
This is a simple yet fully customisable tooltip/pop-up implementation for tkinter widgets. 
It is capable of fully integrating with custom tkinter themes both light and dark ones.

%package -n %name-tests
Summary: Tests for %name
Group: Development/Tools
BuildArch: noarch
Requires: %name = %EVR

%description -n %name-tests
Tests for %name

%package -n %name-docs
Summary: Docs for %name
Group: Development/Tools
BuildArch: noarch
Requires: %name = %EVR

%description -n %name-docs
Docs for %name

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest test/test_%short_name.py

%files
%python3_sitelibdir/%short_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%files -n %name-docs
%doc README.*
%doc docs/
%doc examples/

%changelog
* Fri Nov 29 2024 Yuri Kozyrev <kozyrevid@altlinux.org> 3.1.2-alt1
- initial build
