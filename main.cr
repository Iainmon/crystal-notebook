require "./notebook.cr"
require "aquaplot"
require "random"

include AquaPlot

random = Random.new(69)


# for i in 1..3 do
#   puts i
# end

gender_distribution = {
  male: 10,
  female: 11
}

preferences = {
  male: {
    cats: Array(Float32).new,
    dogs: Array(Float32).new
  },
  female: {
    cats: Array(Float32).new,
    dogs: Array(Float32).new
  }
}

for gender in gender_distribution do
  for n in 0..(gender_distribution[gender]) do
    for preference in preferences[gender].keys.to_a do
      preferences[gender][preference] << random.rand.to_f32
    end
  end
end

scatters = preferences.map do |key, value|
  Scatter.new value[:cats], value[:dogs], title: "#{key}"
end

plt = Plot.new scatters
plt.savefig("images/scatters.png")
plt.close