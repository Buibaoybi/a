-- Minify a Lua script
function minify(input)
    -- Remove single line comments
    input = input:gsub("%-%-.-\n", "\n")

    -- Remove multi-line comments
    input = input:gsub("%-%-%[%[.-%]%]", "")

    -- Remove leading and trailing whitespace
    input = input:gsub("^%s+", ""):gsub("%s+$", "")

    -- Remove extra whitespace
    input = input:gsub("%s+", " ")

    return input
end

-- Example usage
local input = [==[

]==]

local minified = minify(input)
print(minified)