# const/record/immutable macro
# plotter macro
# lambda macro
# this. macro
# baked file system macro
# compose macro

macro fnct(expression);"{{ expression }}";end

macro compose(exp)

end

def lambda(&block)
  block
end

# OR

def lambda(&block : Number -> Number);block;end

def invoke(&block)
  block.call
end

macro compose(lambda_a, lambda_b,...)
  &lambda_a &lambda_b &lambda_c
end

# or struct
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

  def evaluate(domain = -10..10, step : 0.1)
    range = {} of Float64 => Float64
    for x : Float64 = domain.begin, x <= domain.end, x += step do

    end
  end

end

macro lambda(expression);Lambda.new("{{ expression }}") { |x| {{ expression }} };end

f = lambda { |x| x**2 + 1 }
