%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-sensor-msgs-py
Version:        4.5.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS sensor_msgs_py package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-numpy
Requires:       ros-rolling-sensor-msgs
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-rolling-ament-copyright
BuildRequires:  ros-rolling-ament-flake8
BuildRequires:  ros-rolling-ament-pep257
%endif

%description
A package for easy creation and reading of PointCloud2 messages in Python.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Thu May 19 2022 Geoffrey Biggs <geoff@openrobotics.org> - 4.5.0-1
- Autogenerated by Bloom

* Fri Apr 29 2022 Geoffrey Biggs <geoff@openrobotics.org> - 4.4.0-1
- Autogenerated by Bloom

* Thu Mar 31 2022 Geoffrey Biggs <geoff@openrobotics.org> - 4.2.1-1
- Autogenerated by Bloom

* Wed Mar 30 2022 Geoffrey Biggs <geoff@openrobotics.org> - 4.2.0-1
- Autogenerated by Bloom

* Sat Mar 26 2022 Geoffrey Biggs <geoff@openrobotics.org> - 4.1.1-1
- Autogenerated by Bloom

* Tue Mar 01 2022 Geoffrey Biggs <geoff@openrobotics.org> - 4.1.0-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Geoffrey Biggs <geoff@openrobotics.org> - 4.0.0-2
- Autogenerated by Bloom

