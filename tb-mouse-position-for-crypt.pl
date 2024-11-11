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
# Total Battle - Mouse Position Locator
#
#use strict;
no strict;
#
#use warnings;
use v5.14;
no warnings 'uninitialized';

use Win32::Sound;

#Win32::Sound::Play("SystemStart");

srand(time());

$| = 1;

#
# Mouse 32-bit API
#
use Win32::API;

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

my @crypt_menu_first  = qw{975 445};
my @crypt_menu_second = qw{975 525};
my @crypt_menu_third  = qw{975 605};
my @crypt_menu_fourth = qw{975 685};


my @desktop_telescope_mouse_xy                 = qw( 570 905 );
my @desktop_crypt_menu_mouse_xy                = qw( 575 520 );

my @desktop_crypt_menu_first_mouse_xy          = qw( 1100 530 );
my @desktop_crypt_menu_second_mouse_xy         = qw( 1100 632 );
my @desktop_crypt_menu_third_mouse_xy          = qw( 1100 730 );
my @desktop_crypt_menu_fourth_mouse_xy         = qw( 1100 830 );

my @desktop_crypt_first_mouse_xy               = @desktop_crypt_menu_third_mouse_xy;

#my @desktop_crypt_first_mouse_xy              = qw( 1100 530 );

my @desktop_crypt_middle_mouse_xy              = qw( 840 587 );
my @desktop_crypt_middle_mouse_lower_xy        = qw( 890 613 );

my @desktop_crypt_explore_right_mouse_xy       = qw( 1020 830 );
my @desktop_crypt_misclick_top_menu_mouse_xy   = qw( 1122 410 );
my @desktop_crypt_speedup_top_menu_mouse_xy    = qw( 1120 212 );

my @desktop_crypt_speedup_first_mouse_xy       = qw( 1010 510 );
my @desktop_crypt_speedup_second_mouse_xy      = qw( 1010 624 );
my @desktop_crypt_speedup_third_mouse_xy       = qw( 1010 624 );#

my @desktop_crypt_speedup_close_mouse_xy       = qw( 1106 335 );


sub main()
{
	# Record 10 mouse positions delayed by 300 ms
	my $max = 12;

	#Win32::Sound::Play("SystemStart");

	#usleep(300000); # 300 ms
	Win32::Sound::Play("SystemStart");

	for(my $i = 1; $i <= $max; ++$i)
	{
		my $pt = getMouseXYCoordinates();
		print "[$i]\n";

		if(0)
		{
			if ($i == 1)
			{
				SetCursorPos($crypt_menu_first[0], $crypt_menu_first[1]);
			}
			elsif ($i == 2)
			{
				SetCursorPos($crypt_menu_second[0], $crypt_menu_second[1]);
			}
			elsif ($i == 3)
			{
				SetCursorPos($crypt_menu_third[0], $crypt_menu_third[1]);
			}
			elsif ($i == 4)
			{
				SetCursorPos($crypt_menu_fourth[0], $crypt_menu_fourth[1]);
			}
		}

		usleep(300000); # 300 ms
		Win32::Sound::Play("SystemStart");
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
