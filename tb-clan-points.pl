#!perl

use strict;
use warnings;
use Data::Dumper;

#
# PASTE TSV between multiline EOF
#
my $points_tsv=<<EOF;
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
More	6543
Name with spaces	2222
EOF
;

sub main()
{
	my @lines   = split /[\r\n]+/, $points_tsv;
	my %hashmap = ();

	for my $line (@lines)
	{
		chomp($line);

		# Must have at least 2 Excel TSV columns
		if ($line !~ m/\t+/m)
		{
			# print "SKIP[$line]\n";
			next;
		}

		# Keep only first 2 Excel TSV columns
		my ($nickname, $score) = split /\t+/, $line;

		# Strip the parts
		chomp($nickname);
		chomp($score);

		# Clean up nickname
		$nickname =~ s/[^\w\!\#\@\$\&\*\+\.,\- ]+/ /gmi;
		$nickname = ucfirst($nickname);

		# Clean up score (should be NOOP)
		$score =~ s/\D+/ /gmi;

		# Store display key as 000000000 for sorting purposes
		my $display = sprintf("%09d", $score);

		# Store in hashmap for sorting
		$hashmap{$display} = [ $nickname, $score, $display ];
	}

	# Display score in descending order
	for my $key (reverse sort keys %hashmap)
	{
		my ($nickname, $score, $display) = @{ $hashmap{$key} };

		printf("%-30s\t%9d\n", $nickname, $score);

		# Stop displaying once score are way too low...
		if ($score < 10) { last; }
	}
}

main();
exit();
1;

