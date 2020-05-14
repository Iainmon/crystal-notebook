macro for(definition, condition, incrimentation, &block)
  {{definition}}
  while {{condition}}
    {{block.body}}
    {{incrimentation}}
  end
end

# TODO: make ability to also iterate named tuple.
# macro for(expr)
#   ({{expr.args.first.args.first}}).each do |{{expr.name.id}}|
#     {{expr.args.first.block.body}}
#   end
# end


# for ( n (in my_list do) )

macro for(expr)
  ({{expr.args.first.args.first}}).each do |{{expr.name.id}}|
    {{expr.args.first.block.body}}
  end
end


# macro method_alias(new_method, old_method)
#   def {{ new_method }}(*args)
#     {{ old_method }}(*args)
#   end
# end

# method_alias sin, Math.sin

macro method_alias(expression)
  def {{ expression.target }}(*args)
    {{ expression.value }}(*args)
  end
end