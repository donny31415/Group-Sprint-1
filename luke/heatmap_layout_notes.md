# Heat map block layout tests

All four tests use the same data (the neural network's xG for 2025/26), the same colour scale and the same minimum of 5 shots per block. Only the size and position of the blocks changes. The images show Crystal Palace, and the red crosses mark where penalties are recorded (x = 106.2, y = 40).

## Test 1: 6 × 10 unit blocks (6 bands × 8 channels)
The first layout. Blocks were 6 units deep and 10 units wide, covering x = 84 to the goal line across the full width, giving 48 blocks per team. The edges lined up with the penalty area (x = 102) and the six-yard box. It had two problems. Penalties are recorded at y = 40, exactly on the edge between two channels, so which block they landed in depended on how the plotting library handled the edge: mplsoccer put them in the 30–40 channel, whereas plain numpy put them in the 40–50 channel. The wide channels also held almost no shots, so they were grey for every team, and 54% of all blocks were grey (median 2.5 shots per block).

## Test 2: 5 rows × 7 columns, rows 6 units deep
Seven equal columns, with an odd number so that the centre of the pitch falls in the middle of a column and not on an edge. This fixed the penalty problem: all 92 penalties land in the middle column. Rows were 6 units deep starting at x = 90, so shots from further out were counted in the back row (about 9% of all shots). 52% of blocks were grey (median 4 shots). The new problem was that the drawn penalty spot (x = 108) sits on a row edge, while the penalties are recorded just inside the row below, so the dot and the penalties did not appear to line up.

## Test 3: 5 rows × 7 columns, rows 9.2 units deep
Rows were made deeper (starting at x = 74) so that the recorded penalty position (x = 106.2) sits at the exact centre of a block. This worked for the data, but the drawn penalty spot then sat on top of the goals label in that block (for example Arsenal's "19g" appeared as "1•9g"). The back row, from x = 74 to 83, was grey for every team because almost no shots come from that far out. This was the worst layout for grey blocks: 59% (median 2 shots).

## Test 4: 5 rows × 7 columns, rows 8 units deep (final)
Rows start at x = 80 and are 8 units deep, so the drawn penalty spot (x = 108) sits at the centre of its block, between the goals and xG labels. The recorded penalties (x = 106.2) fall in the same block, so all 92 penalties are in one clear block with no overlap. The back row now holds some shots (grey for 68% of teams, not all), and 53% of blocks overall are grey (median 4 shots). The one cost is that the row edge falls at x = 104, so it no longer lines up with the edge of the penalty area at x = 102. We chose this layout because it removes the edge problem, keeps the dot and the labels readable, and has fewer grey blocks than Tests 1 and 3.
