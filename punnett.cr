require "./notebook.cr"

ALPHABET = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

puts "Input genotype A:"
genome_a = gets.to_s.chars
puts "Input genotype B:"
genome_b = gets.to_s.chars

raise "Cannot have an odd genotype!" if (genome_a.size + genome_b.size) % 2 > 0
raise "Genomes must be the same size!" unless genome_a.size == genome_b.size

def isolate_alleles(genome)
    allels = Array(Array(Char)).new
    for i = 0, i < genome.size - 1, i += 2 do
        allels << genome[i..(i + 1)]
    end
    return allels
end

def permute_alleles(allele_group)
    permutations = Array(Array(Char)).new
    for i in allele_group.first do
        for j in allele_group.last do
            permutations << [i, j]
        end
    end
    return permutations
end

def combine_genotypes(allele_group_a, allele_group_b)
    genotypes = Array(Array(Char)).new
    for gene_a in allele_group_a do
        for gene_b in allele_group_b do
            genotypes << gene_a + gene_b
        end
    end
    return genotypes
end

alleles_a = permute_alleles(isolate_alleles genome_a)
alleles_b = permute_alleles(isolate_alleles genome_b)

genotypes = combine_genotypes(alleles_a, alleles_b).map do |gene|
    gene.sort { |a, b| ALPHABET.index(a.to_s).not_nil! <=> ALPHABET.index(b.to_s).not_nil! }
end

frequency_table = Hash(String, Int32).new

for expanded_genotype in genotypes do

    genotype = expanded_genotype.join

    if frequency_table.has_key? genotype
        frequency_table[genotype] += 1
    else
        frequency_table[genotype] = 1
    end
end

probability_table = Hash(String, String).new

for genotype in frequency_table.keys.to_a do
    occurances = frequency_table[genotype].to_f
    probability = occurances / genotypes.size.to_f * 100.to_f
    probability_table[genotype] = "#{ probability.round(2) }%"
end

def genotype_classification(genotype)
    return "heterozygous" unless genotype.first == genotype.last
    return "homozygous dominant" unless genotype.first.lowercase?
    "homozygous recessive"
end

puts "\n"
for genotype in probability_table.keys.to_a do
    probability = probability_table[genotype]
    puts "#{genotype} => #{probability} (#{ genotype_classification genotype.chars[0..1] }, #{ genotype_classification genotype.chars[2..3] })"
end