@rem = '--*-Perl-*--
@echo off
if "%OS%" == "Windows_NT" goto WinNT
perl -x -S "%0" %1 %2 %3 %4 %5 %6 %7 %8 %9
goto endofperl
:WinNT
perl -x -S %0 %*
if NOT "%COMSPEC%" == "%SystemRoot%\system32\cmd.exe" goto endofperl
if %errorlevel% == 9009 echo You do not have Perl in your PATH.
if errorlevel 1 goto script_failed_so_exit_with_non_zero_val 2>nul
goto endofperl
@rem ';
#!perl -w
#line 15
#########################################################################################
# The code above is valid Perl5 where you simply put all the MS-DOS Console Batch junk
# inside a Perl array called "@rem", which is simply discarded and ignored
# and also a valid Batch command line with remarks / comments or @rem
# that will simply call the Perl5 command line on itself.
#########################################################################################


#########################################################################################
# If this Perl script was run using a PHP interpreter by mistake, just exit(1)
# and halt the PHP compiler like right now.
#########################################################################################
#<?php exit(1);__halt_compiler(); ?>
#########################################################################################

#########################################################################################
#
# Redeclare @rem fake array to ensure Perl5 strict mode works properly.
#
#########################################################################################

my @rem = ();

#########################################################################################
#
# Enforce Perl5 strict mode with warnings
#
#########################################################################################

use strict;
use warnings;
use Data::Dumper;

#########################################################################################
#
#
# PASTE your Excel TSV columns between the multiline EOF below...
#
#
#########################################################################################

my $points_tsv=<<EOF;


EOF
;

my %countHash=();

#
# Point HashMap
#
my %pointHash = (

	# Normal Crypt
	'c25'  => 19,
	'c20'  =>  7,
	'c15'  =>  3,
	'c10'  =>  0,
	'c5'   =>  0,

	# Rare Crypt
	'rc35' => 126,
	'rc30' => 70,
	'rc25' => 32,
	'rc20' => 17,
	'rc15' => 10,
	'rc10' =>  0,
	'rc5'  =>  0,

	# Epic Crypt
	'ec35' => 126,
	'ec30' => 60,
	'ec25' => 32,
	'ec20' => 17,
	'ec15' => 10,
	'ec10' =>  0,
	'ec5'  =>  0,

	# Citadel
	'k35'   =>  60,
	'k30'   =>  60,
	'k25'   =>  24,
	'k20'   =>  11,
	'k15'   =>  4,
	'k10'   =>  0,

	# Citadel
	'cit35' =>  60,
	'cit30' =>  60,
	'cit25' =>  24,
	'cit20' =>  11,
	'cit15' =>  4,
	'cit10' =>  0,

	# Cursed Citadel
	'cursed35' =>  60,
	'cursed30' =>  60,
	'cursed25' =>  24,
	'cursed20' =>  11,
	'cursed15' =>  4,
	'cursed10' =>  0,

	#HERO
	'heroic17' => 11,

	''     =>  0
);

sub parseItems()
{
	# Split by lines
	my @list = split /[\r\n]+/, $points_tsv;

	my $points = 0;

	# Loop over all lines
	foreach my $item ( @list )
	{
		chomp $item;

		# Trim spaces
		$item =~ s/^\s+|\s+$//gm;

		# Match item lines by known hash key prefix
		if (($item =~ m/^\s*([rcek]+i?t?a?d?e?l?|cursed)\s*([123450]+)\s*/mi)
		||  ($item =~ m/^\s*(hero?i?c?)\s*([0-9]+)\s*/mi))
		{
			# This will group match either RegExp above that first matches in order
			my $type = $1;
			my $val  = $2;

			# Strip citadel key
			$type =~ s/citad?e?l?\s*$/cit/gm;

			# Reconstitute hash key after stripping
			my $key  = "$type$val";

			# Must be level 5 to 45 inclusive
			if (($val >= 5) && ($val <= 45))
			{
				print "[$key]:[$item]\n";
				if (!defined($countHash{$key}))
				{
					$countHash{$key} = 1;
				}
				else
				{
					$countHash{$key}++;
				}

				my $pt = $pointHash{$key};
				if (defined($pt))
				{
					$points += $pt;
				}
			}
			else
			{
				print "SKIP[$item]\n";
			}
		}
		# Strip comment line
		elsif ($item =~ m/^\s*([xyhH\@]+)([0-9]+)\s*/mi)
		{
			print "KNOWN INVALID[$item]\n";
		}
		elsif ($item eq "")
		{
			#print "EMPTY[$item]\n";
		}
		else
		{
			print "BAD INVALID[$item]\n";
		}
	}

	print Dumper \%countHash;
	print "\n[$points]\n";

	return \%countHash;
}

sub countPoints()
{
	my $points2 = 0;
	foreach my $k (sort keys %countHash)
	{
		my $nb2 = $countHash{$k};
		my $pt2 = $pointHash{$k};

		if (!defined($nb2)) { $nb2 = 0; }
		if (!defined($pt2)) { $pt2 = 0; }

		my $t2  = (0+$nb2) * (0+$pt2);
		print "[$k] : [$nb2] * [$pt2] = [$t2]\n";
		$points2 += $t2;
	}

	print "points2 : [$points2]\n";

	return \%countHash;
}

sub main()
{
	parseItems();
	countPoints();
}

#########################################################################################
#
# Perl script Main / Exit entry points
#
#########################################################################################

main();
exit();
1;

#########################################################################################
#
# Perl script compilation ends right here...
#
#########################################################################################
__END__
:endofperl

@if [%NOPAUSE%]==[1] goto endofscript

@pause

:endofscript
