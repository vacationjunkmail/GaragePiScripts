use strict;
use Data::Dumper;
#my @mission_data = ();
#$mission_data['2018'] = [name=>'test',game=>'ff'];
#print($mission_data['2018']->[1]);
#print("\n");

my %mission_data = ();
#$mission_data{2018}{'2018.1'}='test';
push @{$mission_data{2018}{2018.1}},["number 1"];
push @{$mission_data{2018}{2018.1}},["number 2"];
push @{$mission_data{2018}{2018.2}},"number 2"; 
print Dumper($mission_data{'2018'});
print("\n");
print($mission_data{2018}{2018.1}->[0]);
print("\n");
