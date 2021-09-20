lead='^\/\/ modint start$'
tail='^\/\/ modint end$'
sed -e "/$lead/,/$tail/{ /$lead/{p; r modint.hpp
        }; /$tail/p; d }" test_modint_o.cpp > test_modint.cpp