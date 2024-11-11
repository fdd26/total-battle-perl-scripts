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
use POSIX qw(strftime);
#use Time::Piece;
#use DateTime;

#########################################################################################
#
#
# Total Battle - Mouse Click Crypter for 1536x864 Chrome browser with bookmark tab offset
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

sub moveMouseCursorPosition($$)
{
	my ($x, $y) = @_;
	print "\nMoving cursor to ($x, $y)\n";
	my $b = SetCursorPos($x, $y) or die("GetCursorPos failed: " . $^E);
	return $b;
}

sub getMouseXYCoordinates()
{
	#### using Win32 OO semantics
	my $pt = Win32::API::Struct->new('POINT');
	my $b = GetCursorPos($pt) or die("GetCursorPos failed: " . $^E);
	print "Cursor [$b] is at: ". $pt->{'x'} .", ". $pt->{'y'} ."\n";
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

#################################################################
# HALF SCREEN LEFT 100% CHROME / 25% GAME ZOOM
#################################################################

# 0 means no random swing
my $mouse_delta_x_swing = 0;
my $mouse_delta_y_swing = 0;

my $PYTHON3_PATH_EXE    = q{C:\Progra~1\Python312\python.exe};

#################################################################

my @half_left_telescope_mouse_xy              = qw( 286 722 );
my @half_left_crypt_menu_mouse_xy             = qw( 276 419 );
my @half_left_crypt_first_mouse_xy            = qw( 710 428 );
my @half_left_crypt_middle_mouse_xy           = qw( 497 470 );
my @half_left_crypt_explore_right_mouse_xy    = qw( 643 669 );
my @half_left_crypt_speedup_top_menu_mouse_xy = qw( 726 186 );

my @half_left_crypt_speedup_first_mouse_xy    = qw( 630 410 );
my @half_left_crypt_speedup_second_mouse_xy   = qw( 630 502 );
my @half_left_crypt_speedup_third_mouse_xy    = qw( 630 592 );

my @half_left_crypt_speedup_close_mouse_xy    = qw( 714 271 );

#################################################################
# FULL SCREEN 100% CHROME / 25% GAME ZOOM + Chrome Bookmark bar
#################################################################

my @full_telescope_mouse_xy                   = qw( 564 727 );
my @full_crypt_menu_mouse_xy                  = qw( 542 435 );

my @full_crypt_menu_first_mouse_xy            = qw( 975 445 );
my @full_crypt_menu_second_mouse_xy           = qw( 975 525 );
my @full_crypt_menu_third_mouse_xy            = qw( 975 605 );
my @full_crypt_menu_fourth_mouse_xy           = qw( 975 685 );

my @full_crypt_first_mouse_xy                 = @full_crypt_menu_third_mouse_xy;

#my @full_crypt_first_mouse_xy                = qw( 975 445 );

my @full_crypt_middle_mouse_xy                = qw( 773 488 );
my @full_crypt_middle_mouse_lower_xy          = qw( 970 604 );

my @full_crypt_explore_right_mouse_xy         = qw( 916 686 );
my @full_crypt_misclick_top_menu_mouse_xy     = qw( 995 348 );
my @full_crypt_speedup_top_menu_mouse_xy      = qw( 995 200 );

my @full_crypt_speedup_first_mouse_xy         = qw( 899 430 );
my @full_crypt_speedup_second_mouse_xy        = qw( 899 517 );
my @full_crypt_speedup_third_mouse_xy         = qw( 899 606 );

my @full_crypt_speedup_close_mouse_xy         = qw( 984 284 );

#################################################################

sub validate_is_crypt_left_menu()
{
	my $python3 = $PYTHON3_PATH_EXE;
	my $script  = q{Is-Crypt-Left-Menu.py};
	my @lines   = qx($python3 $script);
	my $output  = join('\n', @lines);

	if ($output =~ m/[\#]+BAD/mi)
	{
		print "is_crypt_left_menu: BAD was found\n";

		print "Crypt Left Menu was not found, the game is stuck\n";
		#exit(1);
		return undef;
	}

	print Dumper \@lines;
	if ($output =~ m/[\(]+([1-9][0-9]*)[, ]+([1-9][0-9]*)[\)]+/mi)
	{
		my $x   = 0 + int($1);
		my $y   = 0 + int($2);
		my @pos = ($x, $y);
		print "is_crypt_left_menu: Found ($x, $y)\n";
		print Dumper \@pos;
		return \@pos;
	}

	return undef;
}

#################################################################

sub validate_is_crypt_gray_title()
{
	my $python3 = $PYTHON3_PATH_EXE;
	my $script  = q{Is-Crypt-Gray-Title.py};
	my @lines   = qx($python3 $script);
	my $output  = join('\n', @lines);

	if ($output =~ m/[\#]+BAD/mi)
	{
		print "is_crypt_gray_title: BAD was found\n";
		return undef;
	}

	print Dumper \@lines;
	if ($output =~ m/[\(]+([1-9][0-9]*)[, ]+([1-9][0-9]*)[\)]+/mi)
	{
		my $x   = 0 + int($1);
		my $y   = 0 + int($2);
		my @pos = ($x, $y);
		print "is_crypt_gray_title: Found ($x, $y)\n";
		print Dumper \@pos;
		return \@pos;
	}

	return undef;
}

#################################################################

sub validate_is_crypt_green_misclick_title()
{
	my $python3 = $PYTHON3_PATH_EXE;
	my $script  = q{Is-Crypt-Green-Misclick-Title.py};
	my @lines   = qx($python3 $script);
	my $output  = join('\n', @lines);

	if ($output =~ m/[\#]+BAD/mi)
	{
		print "is_crypt_green_misclick_title: BAD was found\n";
		return undef;
	}

	print Dumper \@lines;
	if ($output =~ m/[\(]+([1-9][0-9]*)[, ]+([1-9][0-9]*)[\)]+/mi)
	{
		my $x   = 0 + int($1);
		my $y   = 0 + int($2);
		my @pos = ($x, $y);
		print "is_crypt_green_misclick_title: Found ($x, $y)\n";
		print Dumper \@pos;
		return \@pos;
	}

	return undef;
}

#################################################################

sub validate_is_crypt_green_speedup_title()
{
	my $python3 = $PYTHON3_PATH_EXE;
	my $script  = q{Is-Crypt-Green-Speedup-Title.py};
	my @lines   = qx($python3 $script);
	my $output  = join('\n', @lines);

	if ($output =~ m/[\#]+BAD/mi)
	{
		print "is_crypt_green_speedup_title: BAD was found\n";
		return undef;
	}

	print Dumper \@lines;
	if ($output =~ m/[\(]+([1-9][0-9]*)[, ]+([1-9][0-9]*)[\)]+/mi)
	{
		my $x   = 0 + int($1);
		my $y   = 0 + int($2);
		my @pos = ($x, $y);
		print "is_crypt_green_speedup_title: Found ($x, $y)\n";
		print Dumper \@pos;
		return \@pos;
	}

	return undef;
}

#################################################################

sub find_crypt_position()
{
	my $python3 = $PYTHON3_PATH_EXE;
	my $script  = q{crypt-search.py};
	my @lines   = qx($python3 $script);
	my $output  = join('\n', @lines);

	if ($output =~ m/[\#]+BAD/mi)
	{
		print "find_crypt_position: BAD was found\n";
		return undef;
	}

	print Dumper \@lines;
	if ($output =~ m/[\(]+([1-9][0-9]*)[, ]+([1-9][0-9]*)[\)]+/mi)
	{
		my $x   = 0 + int($1);
		my $y   = 0 + int($2);
		my @pos = ($x, $y);
		print "find_crypt_position: Found ($x, $y)\n";
		print Dumper \@pos;
		return \@pos;
	}

	return undef;
}

#################################################################

sub half_left_state_machine()
{
	my @telescope_mouse_xy               = @half_left_telescope_mouse_xy;
	my @crypt_menu_mouse_xy              = @half_left_crypt_menu_mouse_xy;
	my @crypt_first_mouse_xy             = @half_left_crypt_first_mouse_xy;
	my @crypt_middle_mouse_xy            = @half_left_crypt_middle_mouse_xy;
	my @crypt_middle_mouse_lower_xy      = @full_crypt_middle_mouse_lower_xy;
	my @crypt_explore_right_mouse_xy     = @half_left_crypt_explore_right_mouse_xy;

	my @crypt_misclick_top_menu_mouse_xy = @full_crypt_misclick_top_menu_mouse_xy;
	my @crypt_speedup_top_menu_mouse_xy  = @half_left_crypt_speedup_top_menu_mouse_xy;

	my @crypt_speedup_first_mouse_xy     = @half_left_crypt_speedup_first_mouse_xy;
	my @crypt_speedup_second_mouse_xy    = @half_left_crypt_speedup_second_mouse_xy;
	my @crypt_speedup_third_mouse_xy     = @half_left_crypt_speedup_third_mouse_xy;

	my @crypt_speedup_close_mouse_xy     = @half_left_crypt_speedup_close_mouse_xy;

	# RANDOM offset of [-x, x]
	my $dx = int(rand($mouse_delta_x_swing * 2)) - int($mouse_delta_x_swing);
	my $dy = int(rand($mouse_delta_y_swing * 2)) - int($mouse_delta_y_swing);

	my $dw = 150000 + int(rand(100000)); # 150 ms to 250 ms wait delta

	my $wait_move_xy = $dw +    10000; # 10 ms
	my $wait_click   = $dw +    60000; # 60 ms
	my $wait_screen  = $dw +   800000; # 800 ms
	my $wait_crypt   = $dw + 28000000; # 28000 ms

	my @crypt_speedup_mouse_xy = @crypt_speedup_second_mouse_xy;

	moveMouseCursorPosition( $telescope_mouse_xy[0]              + $dx, $telescope_mouse_xy[1]           + $dy );
	usleep($wait_move_xy);
	sendMouseLeftClick(0,0);
	usleep($wait_click);

	usleep($wait_screen);

	moveMouseCursorPosition( $crypt_menu_mouse_xy[0]             + $dx, $crypt_menu_mouse_xy[1]          + $dy );
	usleep($wait_move_xy);
	sendMouseLeftClick(0,0);
	usleep($wait_click);

	usleep($wait_screen);

	my $crypt_left_menu_pos_ref = validate_is_crypt_left_menu();
	if (!defined($crypt_left_menu_pos_ref))
	{
		print "Could not find the crypt LEFT MENU, try again\n";
		#exit(1);
		return 1;
	}

	usleep($wait_screen); # 500 ms

	moveMouseCursorPosition( $crypt_first_mouse_xy[0]          + $dx, $crypt_first_mouse_xy[1]         + $dy );
	usleep($wait_move_xy);
	sendMouseLeftClick(0,0);
	usleep($wait_click);

	usleep($wait_screen);

	usleep($wait_screen);

	moveMouseCursorPosition( $crypt_middle_mouse_xy[0]           + $dx, $crypt_middle_mouse_xy[1]        + $dy );
	usleep($wait_move_xy);
	sendMouseLeftClick(0,0);
	usleep($wait_click);

	usleep($wait_screen);

	my $crypt_gray_title_pos_ref = validate_is_crypt_gray_title();

	if (!defined($crypt_gray_title_pos_ref))
	{
		my $crypt_misclick_green_title_pos_ref = validate_is_crypt_green_misclick_title();
		if (!defined($crypt_gray_title_pos_ref))
		{
			print "Could not find the crypt, nor misclick green title, try again\n";
			return 21;
		}
		elsif (0)
		{
			my @crypt_misclick_green_title_pos = @{$crypt_misclick_green_title_pos_ref};
			print "Misclick green title window was found at [" . $crypt_misclick_green_title_pos[0] .",". $crypt_misclick_green_title_pos[1] . "]\n";

			# Cursor is at: 994, 348
			moveMouseCursorPosition( $crypt_misclick_top_menu_mouse_xy[0] + $dx, $crypt_misclick_top_menu_mouse_xy[1] + $dy );
			usleep($wait_move_xy);
			sendMouseLeftClick(0,0);
			usleep($wait_click);

			usleep($wait_screen);

			my $crypt_misclick_green_title_pos_ref2 = validate_is_crypt_green_misclick_title();
			if (!defined($crypt_misclick_green_title_pos_ref2))
			{
				print "Misclick window was closed\n";

				print "MOVE MOUSE LOWER [". $crypt_middle_mouse_lower_xy[0] .",". $crypt_middle_mouse_lower_xy[1] . "]\n";

				#my @full_crypt_middle_mouse_xy                = qw( 773 488 );
				# 970, 604
				moveMouseCursorPosition( $crypt_middle_mouse_lower_xy[0]  + $dx, $crypt_middle_mouse_lower_xy[1]      + $dy );
				usleep($wait_move_xy);
				sendMouseLeftClick(0,0);
				usleep($wait_click);

				usleep($wait_screen);

				print "Validate Crypt Gray Title #2\n";

				my $crypt_gray_title_pos_ref2 = validate_is_crypt_gray_title();
				print Dumper $crypt_gray_title_pos_ref2;
				if (!defined($crypt_gray_title_pos_ref2))
				{
					return 23;
				}
				else
				{
					print "Crypt was shifted below\n";
				}
			}
			else
			{
				print "Could not find the lower crypt, try again\n";
				return 22;
			}
		}
		else
		{
			print "Could not find the crypt, try again\n";
			return 20;
		}
	}

	#usleep($wait_screen); # 500 ms

	moveMouseCursorPosition( $crypt_explore_right_mouse_xy[0]  + $dx, $crypt_explore_right_mouse_xy[1] + $dy );
	usleep($wait_move_xy);
	sendMouseLeftClick(0,0);
	usleep($wait_click);

	usleep($wait_screen);

	moveMouseCursorPosition( $crypt_speedup_top_menu_mouse_xy[0] + $dx, $crypt_speedup_top_menu_mouse_xy[1] + $dy );
	usleep($wait_move_xy);
	sendMouseLeftClick(0,0);
	usleep($wait_click);

	usleep($wait_screen);

	#usleep($wait_screen);

	moveMouseCursorPosition( $crypt_speedup_mouse_xy[0]          + $dx, $crypt_speedup_mouse_xy[1]       + $dy );
	usleep($wait_move_xy);

	#usleep($wait_screen);

	my $crypt_green_title_pos_ref = validate_is_crypt_green_speedup_title();

	if (!defined($crypt_green_title_pos_ref))
	{
		print "Could not find the speed up title, try again\n";
		return 3;
	}

	sendMouseLeftClick(0,0);
	usleep($wait_click);

	# 5 speed up clicks
	usleep($wait_click);
	sendMouseLeftClick(0,0);
	usleep($wait_click);
	sendMouseLeftClick(0,0);
	usleep($wait_click);
	sendMouseLeftClick(0,0);
	usleep($wait_click);
	sendMouseLeftClick(0,0);
	usleep($wait_click);
	sendMouseLeftClick(0,0);
	usleep($wait_click);
	usleep($wait_click);

	usleep($wait_screen);

	Win32::Sound::Play("SystemStart");

	usleep($wait_screen);

	moveMouseCursorPosition( $crypt_speedup_close_mouse_xy[0]  + $dx, $crypt_speedup_close_mouse_xy[1] + $dy );
	usleep($wait_move_xy);
	sendMouseLeftClick(0,0);
	usleep($wait_click);
	usleep($wait_screen);

	Win32::Sound::Play("SystemStart");
	usleep($wait_crypt);
	Win32::Sound::Play("SystemStart");

	return 0;
}

#################################################################

sub full_screen_state_machine(;$;$)
{
	my $i = $_[0];
	if (!defined($i))
	{
		$i = -1;
	}
	else
	{
		$i = int($i) % 4;
	}

	my $skip = $_[1];
	if (!defined($skip))
	{
		$skip = 0;
	}
	else
	{
		$skip = 0 + int($skip);
	}

	if ($i >= 0)
	{
		if ($i == 1)
		{
			@full_crypt_first_mouse_xy = @full_crypt_menu_second_mouse_xy;
		}
		elsif ($i == 2)
		{
			@full_crypt_first_mouse_xy = @full_crypt_menu_third_mouse_xy;
		}
		elsif ($i == 3)
		{
			@full_crypt_first_mouse_xy = @full_crypt_menu_fourth_mouse_xy;
		}
		else
		{
			@full_crypt_first_mouse_xy = @full_crypt_menu_first_mouse_xy;
		}
	}

	my @telescope_mouse_xy               = @full_telescope_mouse_xy;
	my @crypt_menu_mouse_xy              = @full_crypt_menu_mouse_xy;
	my @crypt_first_mouse_xy             = @full_crypt_first_mouse_xy;
	my @crypt_middle_mouse_xy            = @full_crypt_middle_mouse_xy;
	my @crypt_middle_mouse_lower_xy      = @full_crypt_middle_mouse_lower_xy;
	my @crypt_explore_right_mouse_xy     = @full_crypt_explore_right_mouse_xy;
	my @crypt_misclick_top_menu_mouse_xy = @full_crypt_misclick_top_menu_mouse_xy;
	my @crypt_speedup_top_menu_mouse_xy  = @full_crypt_speedup_top_menu_mouse_xy;

	my @crypt_speedup_first_mouse_xy     = @full_crypt_speedup_first_mouse_xy;
	my @crypt_speedup_second_mouse_xy    = @full_crypt_speedup_second_mouse_xy;
	my @crypt_speedup_third_mouse_xy     = @full_crypt_speedup_third_mouse_xy;

	my @crypt_speedup_close_mouse_xy     = @full_crypt_speedup_close_mouse_xy;

	# RANDOM offset of [-x, x]
	my $dx = int(rand($mouse_delta_x_swing * 2)) - int($mouse_delta_x_swing);
	my $dy = int(rand($mouse_delta_y_swing * 2)) - int($mouse_delta_y_swing);

	my $dw = 150000 + int(rand(100000)); # 150 ms to 250 ms wait delta

	my $wait_move_xy = $dw +    10000; # 10 ms
	my $wait_click   = $dw +    60000; # 60 ms
	my $wait_screen  = $dw +   800000; # 800 ms
	my $wait_crypt   = $dw + 28000000; # 28000 ms

	my @crypt_speedup_mouse_xy = @crypt_speedup_second_mouse_xy;

	if (1)
	{
		if($skip < 1)
		{
			moveMouseCursorPosition( $telescope_mouse_xy[0]              + $dx, $telescope_mouse_xy[1]           + $dy );
			usleep($wait_move_xy);
			sendMouseLeftClick(0,0);
			usleep($wait_click);

			usleep($wait_screen);

			moveMouseCursorPosition( $crypt_menu_mouse_xy[0]             + $dx, $crypt_menu_mouse_xy[1]          + $dy );
			usleep($wait_move_xy);
			sendMouseLeftClick(0,0);
			usleep($wait_click);

			usleep($wait_screen);

			my $crypt_left_menu_pos_ref = validate_is_crypt_left_menu();
			if (!defined($crypt_left_menu_pos_ref))
			{
				print "Could not find the crypt LEFT MENU, try again\n";
				#exit(1);
				return 1;
			}

			usleep($wait_screen); # 500 ms

			moveMouseCursorPosition( $crypt_first_mouse_xy[0]          + $dx, $crypt_first_mouse_xy[1]         + $dy );
			usleep($wait_move_xy);
			sendMouseLeftClick(0,0);
			usleep($wait_click);

			usleep($wait_screen);

			usleep($wait_screen);

			moveMouseCursorPosition( $crypt_middle_mouse_xy[0]           + $dx, $crypt_middle_mouse_xy[1]        + $dy );
			usleep($wait_move_xy);
			sendMouseLeftClick(0,0);
			usleep($wait_click);

			usleep($wait_screen);
		}
		else
		{
			my $crypt_pos_ref = find_crypt_position();
			if (!defined($crypt_pos_ref))
			{
				print "Could not find ANY crypt, try again\n";
				return 3;
			}
			else
			{
				@crypt_middle_mouse_xy = @{ $crypt_pos_ref };

				print "Using NEW CRYPT at = (". ( $crypt_middle_mouse_xy[0] + $dx) . ",". ( $crypt_middle_mouse_xy[1] + $dy ). ");\n";

				moveMouseCursorPosition( $crypt_middle_mouse_xy[0]       + $dx, $crypt_middle_mouse_xy[1]        + $dy );
				usleep($wait_move_xy);
				sendMouseLeftClick(0,0);
				usleep($wait_click);

				usleep($wait_screen);
			}
		}
	}

	my $crypt_gray_title_pos_ref = validate_is_crypt_gray_title();
	print Dumper $crypt_gray_title_pos_ref;

	if (!defined($crypt_gray_title_pos_ref))
	{
		my $crypt_misclick_green_title_pos_ref = validate_is_crypt_green_misclick_title();
		print Dumper $crypt_misclick_green_title_pos_ref;

		if (!defined($crypt_misclick_green_title_pos_ref))
		{
			print "Could not find the crypt, nor misclick green title, try again\n";
			return 21;
		}
		elsif (0)
		{
			my @crypt_misclick_green_title_pos = @{$crypt_misclick_green_title_pos_ref};
			print "Misclick green title window was found at [" . $crypt_misclick_green_title_pos[0] .",". $crypt_misclick_green_title_pos[1] . "]\n";

			# Cursor is at: 994, 348
			moveMouseCursorPosition( $crypt_misclick_top_menu_mouse_xy[0] + $dx, $crypt_misclick_top_menu_mouse_xy[1] + $dy );
			usleep($wait_move_xy);
			sendMouseLeftClick(0,0);
			usleep($wait_click);

			usleep($wait_screen);

			my $crypt_misclick_green_title_pos_ref2 = validate_is_crypt_green_misclick_title();
			if (!defined($crypt_misclick_green_title_pos_ref2))
			{
				print "Misclick window was closed\n";

				print "MOVE MOUSE LOWER [". $crypt_middle_mouse_lower_xy[0] .",". $crypt_middle_mouse_lower_xy[1] . "]\n";

				#my @full_crypt_middle_mouse_xy                = qw( 773 488 );
				# 970, 604
				moveMouseCursorPosition( $crypt_middle_mouse_lower_xy[0]  + $dx, $crypt_middle_mouse_lower_xy[1]      + $dy );
				usleep($wait_move_xy);
				sendMouseLeftClick(0,0);
				usleep($wait_click);

				usleep($wait_screen);

				print "Validate Crypt Gray Title #2\n";

				my $crypt_gray_title_pos_ref2 = validate_is_crypt_gray_title();
				print Dumper $crypt_gray_title_pos_ref2;
				if (!defined($crypt_gray_title_pos_ref2))
				{
					return 23;
				}
				else
				{
					print "Crypt was shifted below\n";
				}
			}
			else
			{
				print "Could not find the lower crypt, try again\n";
				return 22;
			}
		}
		else
		{
			print "Could not find the crypt, try again\n";
			return 20;
		}
	}

	#usleep($wait_screen); # 500 ms

	moveMouseCursorPosition( $crypt_explore_right_mouse_xy[0]  + $dx, $crypt_explore_right_mouse_xy[1] + $dy );
	usleep($wait_move_xy);
	sendMouseLeftClick(0,0);
	usleep($wait_click);

	usleep($wait_screen);

	moveMouseCursorPosition( $crypt_speedup_top_menu_mouse_xy[0] + $dx, $crypt_speedup_top_menu_mouse_xy[1] + $dy );
	usleep($wait_move_xy);
	sendMouseLeftClick(0,0);
	usleep($wait_click);

	usleep($wait_screen);

	#usleep($wait_screen);

	moveMouseCursorPosition( $crypt_speedup_mouse_xy[0]          + $dx, $crypt_speedup_mouse_xy[1]       + $dy );
	usleep($wait_move_xy);

	#usleep($wait_screen);

	my $crypt_green_title_pos_ref = validate_is_crypt_green_speedup_title();

	if (!defined($crypt_green_title_pos_ref))
	{
		print "Could not find the speed up title, try again\n";
		return 3;
	}

	sendMouseLeftClick(0,0);
	usleep($wait_click);

	# 5 speed up clicks
	usleep($wait_click);
	sendMouseLeftClick(0,0);
	usleep($wait_click);
	sendMouseLeftClick(0,0);
	usleep($wait_click);
	sendMouseLeftClick(0,0);
	usleep($wait_click);
	sendMouseLeftClick(0,0);
	usleep($wait_click);
	sendMouseLeftClick(0,0);
	usleep($wait_click);
	usleep($wait_click);

	usleep($wait_screen);

	Win32::Sound::Play("SystemStart");

	usleep($wait_screen);

	moveMouseCursorPosition( $crypt_speedup_close_mouse_xy[0]  + $dx, $crypt_speedup_close_mouse_xy[1] + $dy );
	usleep($wait_move_xy);
	sendMouseLeftClick(0,0);
	usleep($wait_click);
	usleep($wait_screen);

	Win32::Sound::Play("SystemStart");
	usleep($wait_crypt);
	Win32::Sound::Play("SystemStart");

	return 0;
}

#################################################################

sub main()
{
	# Send many crypt mining sequences
	my $max   = 7800;
	my $r2    = 0;
	my $retry = 0;
	my $good  = 0;
	my $total = 0;

	my $pt = getMouseXYCoordinates();

	print "Sleep 5 seconds... GO!\n\n";
	Win32::Sound::Play("SystemStart");
	sleep(5);


	Win32::Sound::Play("SystemStart");

	for(my $i = 1; $i <= $max; ++$i)
	{
		my $pt = getMouseXYCoordinates();
		print "[$i]\t";
		print strftime("%Y-%m-%d %H:%M:%S", localtime(time) );
		print "\t with GOOD [$good] / [$total]";
		print "\n";

		if ($r2 < 1)
		{
			print "Wait 300ms...\n";
			usleep(300000); # 300 ms
		}
		else
		{
			print "Skip wait...\n";
		}

		$r2 = full_screen_state_machine($i % 4);

		if ($r2 == 1)
		{
			++$retry;
			print "BAD RETRY... [$retry] after GOOD [$good] / [$total]\n";
			print strftime("%Y-%m-%d %H:%M:%S", localtime(time) );
			print "\n";
			$good = 0;
		}
		elsif ($r2 == 0)
		{
			++$good;
			++$total;

			if ($good >= 10)
			{
				print "RESET BAD RETRY... [$retry] after GOOD [$good] / [$total]\n";
				$retry = 0;
			}
		}

		if ($retry > 3)
		{
			print "BAD RETRY EXITING... [$retry] after GOOD [$good] / [$total]\n";
			print strftime("%Y-%m-%d %H:%M:%S", localtime(time) );
			print "\n";
			exit(1);
		}

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
