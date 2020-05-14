require "aquaplot"
require "./notebook.cr"

class Lambda

  property proc
  property expression : String

  def initialize(expression, &block : Float64 -> Float64)
    @expression = expression
    @proc = block
  end

  def export
    fnct &proc
  end

  # Plots function on graph
  def plot
  end

  def evaluate(domain = -10..10, step = 0.1)
    range = {} of Float64 => Float64
    for x = domain.begin.to_f64, x <= domain.end.to_f64, x += step do
      range[x] = proc.call x
    end
    return range
  end

end

macro lambda(expression);Lambda.new("{{ expression }}") { |x| {{ expression }} };end

def plots(*lambdas)
  fns = [] of AquaPlot::Function
  for lambd in lambdas do
    fns << AquaPlot::Function.new lambd.expression
  end
  plt = AquaPlot::Plot.new fns
  plt.show
  plt.close
end

require "math"




method_alias sin = Math.sin
f = lambda sin(x)


# f = lambda x**2 + 4


plots = f.evaluate
for pl in plots.keys do
  puts "#{ pl.round(2) } = #{ plots[pl].round(2) }"
end

plots f