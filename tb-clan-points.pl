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

my $POINTS_TSV = <<EOF;
Alice	1
Bob	200
Cat	3000
D	5000
E	100000
F	999999
G	50
H	90
J	100
K	123456
More !!!	6543
Name with spaces	2222
EOF
;

sub main()
{
	my @lines    = split( /[\r\n]+/, $POINTS_TSV );
	my %scoremap = ();

	for my $line ( @lines )
	{
		chomp($line);

		# Must have at least 2 Excel TSV columns
		if ($line !~ m/\t+/m) { next; }

		# Keep only the first 2 Excel TSV columns
		my ($nickname, $score) = split( /\t/, $line );

		# Strip the parts
		chomp($nickname);
		chomp($score);

		# Clean up nickname
		$nickname =~ s/[^\w\!\#\@\$\&\*\+\.,\- ]+/ /gmi;

		# Uppercase first nickname character
		$nickname = ucfirst( $nickname );

		# Clean up the score from non-digit (should be NOOP)
		$score =~ s/\D+/ /gmi;

		# Store the display key as 000000000 for sorting purposes
		my $display = sprintf("%09d", $score);

		# Store values inside a hash map for sorting purposes
		$scoremap{$display} = [ $nickname, $score, $display ];
	}

	# Display score in descending order
	for my $key (reverse sort keys %scoremap)
	{
		# Extract array parts from hash map
		my ($nickname, $score, $display) = @{ $scoremap{$key} };

		# Display with 30 spaces suffix in place, tab, then assume 9 digits score alignment
		printf("%-30s\t%9d\n", $nickname, $score);

		# Stop displaying once the score gets way too low...
		if ($score < 10) { last; }
	}
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
