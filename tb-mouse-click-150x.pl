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
#
# BSD 2-Clause Licensed source code
#
# Copyright (c) 2024, fdd26
#
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
# Total Battle - Daily Job Free Mouse Click repeat x 150 every other seconds
#
#use strict;
no strict;
#
use warnings;
use v5.14;

use Win32::Sound;

#Win32::Sound::Play("SystemStart");

srand(time());

$| = 1;

#
# Mouse 32-bit API
#
use Win32::API;
use Win32::API::Struct;

#
# @see https://stackoverflow.com/questions/896904/how-do-i-sleep-for-a-millisecond-in-perl
#
use Time::HiRes qw(usleep);

#
# @see https://metacpan.org/release/BULKDD/Win32-API-0.84/source/samples/GetCursorPos.pl
#
Win32::API::Struct->typedef( 'POINT' => qw( LONG x; LONG y; ) );
Win32::API->Import('user32' => 'BOOL GetCursorPos(LPPOINT pt)');
Win32::API->Import('user32' => 'BOOL SetCursorPos(int x, int y)');
Win32::API->Import('user32' => 'void mouse_event(int dwFlags, int dx, int dy, int dwData, int dwExtraInfo)');

sub getMouseXYCoordinates()
{
	#### using Win32 OO semantics
	my $pt = Win32::API::Struct->new('POINT');

	# Initialize to avoid warning
	$pt->{'x'} = 0;
	$pt->{'y'} = 0;

	GetCursorPos($pt)  or die("GetCursorPos failed: " . $^E);
	print "Cursor is at: ". $pt->{'x'} .", ". $pt->{'y'} ."\n";
	return $pt;
}

my $MOUSEEVENTF_LEFTDOWN  = 0x02;
my $MOUSEEVENTF_LEFTUP    = 0x04;
my $MOUSEEVENTF_RIGHTDOWN = 0x08;
my $MOUSEEVENTF_RIGHTUP   = 0x10;

sub sendMouseRightClick($$)
{
	my ($mx, $my) = @_;
	my $event = 0x18; # $MOUSEEVENTF_RIGHTDOWN | $MOUSEEVENTF_RIGHTUP;
	mouse_event($event, $mx, $my, 0, 0);
}

sub sendMouseLeftClick($$)
{
	my ($mx, $my) = @_;
	my $event = 0x06; # $MOUSEEVENTF_LEFTDOWN | $MOUSEEVENTF_LEFTUP;
	mouse_event(0x06, $mx, $my, 0, 0);
}

sub main()
{
	# Send 150 mouse clicks delayed by 200 ms + randomized 100 ms
	my $max = 150;

	my $pt = getMouseXYCoordinates();

	my $x = 0;
	my $y = 0;

	if (0)
	{
		$x = 987;
		$y = 378;
	}

	print "MOVE Mouse!\n\n";

	if ($x > 0 && $y > 0)
	{
		SetCursorPos($x, $y);
	}

	print "Sleep 5 seconds... GO!\n\n";

	sleep(5);

	print "MOVE AND CLICK!\n\n";
	if ($x > 0 && $y > 0)
	{
		SetCursorPos($x, $y);
	}

	Win32::Sound::Play("SystemStart");

	for(my $i = 1; $i <= $max; ++$i)
	{
		sendMouseLeftClick($x, $y);
		print "[$i]\n";
		usleep(200000); # 200 ms
		usleep(int(rand(100000))); # up to 100 ms
	}

	Win32::Sound::Play("SystemStart");
}

main();
exit(0);
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
