require "./matplotcr.cr"

# figure = Matplotcr::Figure.new
# lineplot = Matplotcr::LinePlot.new([1, 2, 3], [5.5, 7.6, 11.1])
# lineplot2 = Matplotcr::ScatterPlot.new([1.0, 2.0, 4.5], [1, 2, 3])
# figure.add lineplot
# figure.add lineplot2
# figure.save("test_colour.png")

python_path = "/usr/bin/python3"
font = Matplotcr::RCFont.new "DejaVu Sans", ["normal"]
figure = Matplotcr::Figure.new python_path, font: font

x = [1, 2, 3, 4]
y = [5.5, 7.6, 11.1, 6.5]
lineplot = Matplotcr::ScatterPlot.new(x, y)
figure.add lineplot
points = x.zip(y).map { |a,b| [a, b]}
(0...2).each { |i| figure.add Matplotcr::Annotation.new points[i][0] + 0.1, points[i][1] + 0.1, "$p#{i}$" }

figure.save("test_colour.png")
