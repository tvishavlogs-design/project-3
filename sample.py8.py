team_a = 85
team_b = 92
last_week_total = 160
total_points = team_a +team_b
average_points =total_points / 2
stars_per_box=10
boxes_packed = total_points // stars_per_box
leftover_stars= total_points % stars_per_box
points_growth=total_points - last_week_total
total_points += 15 
print("total points:",total_points)
print("average points:",average_points)
print("growth vs last week ",points_growth)
print("leftover stars:",leftover_stars)