#!/usr/bin/perl

sub init_maze {
  my ($max_row, $max_col) = @_;

  my $maze = [];
  for (my $r=0; $r < $max_row; $r++) {
     for (my $c=0; $c < $max_col; $c++) {
        push @{$maze->[$r]}, {'visited' => 0,
			     'bottom'  => 1,
                             'right'   => 1,
                            };
     }
  }
  return $maze;
}

sub make_maze {
  my ($maze, $row, $col) = @_;

  $maze->[$row]->[$col]->{'visited'} = 1;

  while (my $unvisited = get_unvisited($maze, $row, $col)) {
    last unless @$unvisited;

    # Randomly select a neighbor
    my $choice = $unvisited->[ rand(@$unvisited) ];

    # Knock down the wall between them
    remove_wall($maze, [$row, $col], $choice);

    # move to this new cell
    make_maze($maze, $choice->[0], $choice->[1]);
  }
}

sub get_unvisited {
  my ($maze, $row, $col) = @_;
  my @found;

  # look for neighbors in cardinal directions;
  # be mindful of maze bounderies
  if ($row == 0) {
    push @found, [$row + 1, $col] unless $maze->[$row + 1]->[$col]{'visited'};
  } elsif ($row == @$maze - 1) {
    push @found, [$row - 1, $col] unless $maze->[$row - 1]->[$col]->{'visited'};
  } else {
    if ($row + 1 < @$maze) {
      push @found, [$row + 1, $col] unless $maze->[$row + 1]->[$col]->{'visited'};
    }
    push @found, [$row - 1, $col] unless $maze->[$row - 1]->[$col]->{'visited'};
  }

  if ($col == 0) {
    push @found, [$row, $col + 1] unless $maze->[$row]->[$col + 1]->{'visited'};
  } elsif ($col == (@{$maze->[0]} - 1)) {
    push @found, [$row, $col - 1] unless $maze->[$row]->[$col - 1]->{'visited'};
  } else {
    if ($col + 1 < @{$maze->[0]}) {
      push @found, [$row, $col + 1] unless $maze->[$row]->[$col + 1]->{'visited'};
    }
    push @found, [$row, $col - 1] unless $maze->[$row]->[$col - 1]->{'visited'};
  }

  return \@found;
}

sub remove_wall {
  my ($maze, $r1, $r2) = @_;
  my $selected;

  if ( $r1->[0] == $r2->[0] ) {
    # Rows are equal, must be East/West neighbors
    $selected = ($r1->[1] < $r2->[1]) ? $r1 : $r2;
    $maze->[ $selected->[0] ]->[ $selected->[1] ]->{'right'} = 0;

   } elsif ( $r1->[1] == $r2->[1] ) {
     # Columns are the same, must be North/South neighbors
     $selected = ($r1->[0] < $r2->[0]) ? $r1 : $r2;
     $maze->[ $selected->[0] ]->[ $selected->[1] ]->{'bottom'} = 0;
   } else {
     die("ERROR: bad neighbors ($r1->[0], $r1->[1]) and ($r2->[0], $r2->[1])\n");
   }
   return;
}

sub print_maze {
   my ($maze) = @_;
   my $screen = [];

   my $screen_row = 0;
   for (my $r=0; $r < @$maze; $r++) {
     if ($r == 0) {
       # Top border
       push @{$screen->[$r]}, '+';
       for (@{$maze->[0]}) {
	 push @{$screen->[$r]}, '--', '+';
       }
     }

     for (my $c=0; $c < @{$maze->[0]}; $c++) {
       my @middle;
       if ($c == 0) {
	 push @middle, "|";
       }

       push @middle, "  "; # room center
       if ($maze->[$r]->[$c]->{'right'}) {
	 push @middle, "|";
       } else {
	 push @middle, " ";
       }
       push @{$screen->[$screen_row + 1]}, @middle;

       my @bottom;
       if ($c == 0) {
	 push @bottom, "+";
       }

       if ($maze->[$r]->[$c]->{'bottom'}) {
	 push @bottom, "--";
       } else {
	 push @bottom, "  ";
       }
       push @bottom, "+";
       push @{$screen->[$screen_row + 2]}, @bottom;
     }
     $screen_row += 2;
   }

   for (my $r=0; $r < @$screen; $r++) {
     for (my $c=0; $c < @{$screen->[0]}; $c++) {
       print $screen->[$r]->[$c];
     }
     print "\n";
   }
   print "\n";
}

my $dimension = $ARGV[0] || 5;
my $maze = init_maze($dimension, $dimension);

my ($startRow, $startCol) = (int(rand($dimension)), int(rand($dimension)));
make_maze($maze, $startRow, $startCol, undef);

print_maze($maze);


