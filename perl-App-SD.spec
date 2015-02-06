%define upstream_name    App-SD
%define upstream_version 0.75

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A peer to peer ticket tracking system
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Config::GitLike) >= 1.30.0
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Format::Natural)
BuildRequires:	perl(Email::Address)
BuildRequires:	perl(Email::MIME)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(HTML::Tree)
BuildRequires:	perl(HTML::TreeBuilder) >= 4.100.0
BuildRequires:	perl(LWP::Simple)
BuildRequires:	perl(Net::GitHub) >= 0.280.0
BuildRequires:	perl(Net::Google::Code) >= 0.140.0
BuildRequires:	perl(Net::Jifty) >= 0.90.0
BuildRequires:	perl(Net::Lighthouse) >= 0.10.0
BuildRequires:	perl(Net::Redmine) >= 0.80.0
BuildRequires:	perl(Net::Trac) >= 0.160.0
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Prophet)
BuildRequires:	perl(RT::Client::REST)
BuildRequires:	perl(Test::Script::Run) >= 0.20.0
BuildRequires:	perl(Test::Cukes)
BuildRequires:	perl(Text::Greeking)
BuildRequires:	perl(Time::Progress)
BuildRequires:	perl(Try::Tiny) >= 0.20.0
BuildRequires:	perl(URI::file)
BuildRequires:	perl-Path-Dispatcher-Declarative
# when Net::Trac will be fixed 
# https://rt.cpan.org/Ticket/Display.html?id=57063
#BuildRequires: trac-standalone trac-sqlite
BuildArch:	noarch

%description
SD is a peer to peer ticket tracking system built on the Prophet distributed 
database. SD is designed to make it easy to work with tickets and to share 
ticket databases with your collaborators.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# (misc) check is stalled, didn't found why
rm -f t/server.t
# (misc) requires network access, do not work on iurt
rm -Rf t/sd-lighthouse
rm -Rf t/sd-gcode
rm -Rf t/sd-github
# Fail on ABF anyway
#make test

%install
%makeinstall_std

%files
%doc META.yml Changes README
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/*


%changelog
* Fri May 07 2010 Michael Scherer <misc@mandriva.org> 0.740.0-1mdv2010.1
+ Revision: 543211
- import perl-App-SD


* Thu May 06 2010 cpan2dist 0.74-1mdv
- initial mdv release, generated with cpan2dist
