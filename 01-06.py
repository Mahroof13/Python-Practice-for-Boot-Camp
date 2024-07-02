import matplotlib.pyplot as plt
import numpy as np

# 1. Draw a line in a diagram from position (0,0) to position (6,250)
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
plt.figure()
plt.plot(xpoints, ypoints)
plt.title("Line from (0,0) to (6,250)")
plt.show()

# 2. Draw a line in a diagram from position (1, 3) to position (8, 10)
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.figure()
plt.plot(xpoints, ypoints)
plt.title("Line from (1,3) to (8,10)")
plt.show()

# 3. Draw two points in the diagram, one at position (1, 3) and one in position (8, 10)
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.figure()
plt.plot(xpoints, ypoints, 'o')
plt.title("Two points at (1,3) and (8,10)")
plt.show()

# 4. Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10)
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
plt.figure()
plt.plot(xpoints, ypoints)
plt.title("Line through (1,3), (2,8), (6,1), and (8,10)")
plt.show()

# 5. Plotting without x-points
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.figure()
plt.plot(ypoints)
plt.title("Plotting without x-points")
plt.show()

# 6. Mark each point with a circle
ypoints = np.array([3, 8, 1, 10])
plt.figure()
plt.plot(ypoints, marker='o')
plt.title("Points marked with circles")
plt.show()

# 7. Mark each point with a star
ypoints = np.array([3, 8, 1, 10])
plt.figure()
plt.plot(ypoints, marker='*')
plt.title("Points marked with stars")
plt.show()

# 8. Mark with red dotted line
ypoints = np.array([3, 8, 1, 10])
plt.figure()
plt.plot(ypoints, '*:r')
plt.title("Red dotted line with stars")
plt.show()

# 9. Set the size of the markers to 20
ypoints = np.array([3, 8, 1, 10])
plt.figure()
plt.plot(ypoints, marker='o', ms=20)
plt.title("Markers of size 20")
plt.show()

# 10. Set the EDGE color to red
ypoints = np.array([3, 8, 1, 10])
plt.figure()
plt.plot(ypoints, marker='o', ms=20, mec='r')
plt.title("Edge color set to red")
plt.show()

# 11. Set the FACE color to red
ypoints = np.array([3, 8, 1, 10])
plt.figure()
plt.plot(ypoints, marker='o', ms=20, mfc='r')
plt.title("Face color set to red")
plt.show()

# 12. Set linestyle to dashed, color to green, and linewidth to 20.5
ypoints = np.array([3, 8, 1, 10])
plt.figure()
plt.plot(ypoints, linestyle='dashed', c='#4CAF50', linewidth=20.5)
plt.title("Dashed green line with linewidth 20.5")
plt.show()

# 13. Draw two lines by specifying a plt.plot() function for each line
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.figure()
plt.plot(y1)
plt.plot(y2)
plt.title("Two separate lines")
plt.show()

# 14. Draw two lines by specifying the x- and y-point values for both lines
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
plt.figure()
plt.plot(x1, y1, x2, y2)
plt.title("Two lines with specified x- and y-points")
plt.show()

# 15. Add a plot title and labels for the x- and y-axis
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.figure()
plt.plot(x, y)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()

# 16. Set the line properties of the grid
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.figure()
plt.plot(x, y)
plt.title("Sports Watch Data with Grid")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid(color='green', linestyle='--', linewidth=0.5)
plt.show()

# 17. Making multiple plots with main heading and subheadings
plt.figure()
# Plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("SALES")

# Plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()

# 18. Making two scatter plots on the same figure
plt.figure()
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
plt.scatter(x, y, color='black')

x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
plt.scatter(x, y, color='red')
plt.title("Two scatter plots on the same figure")
plt.show()

# 19. Making bar graphs
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.figure()
plt.bar(x, y, width=1, color="red")
plt.title("Bar Graph")
plt.show()

# 20. Simple pie chart
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.figure()
plt.pie(y, labels=mylabels)
plt.title("Simple Pie Chart")
plt.show()

# 21. Explode with shadows
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.figure()
plt.pie(y, labels=mylabels, explode=myexplode, shadow=True, colors=mycolors)
plt.title("Pie Chart with Explode and Shadows")
plt.show()
