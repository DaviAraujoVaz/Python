htmlLista = [
    "<!DOCTYPE html>\n",
    '<html lang="pt-br">\n',
    "\n",
    "\n",
    "<head>\n",
    '\t<meta charset="utf-8">\n',
    "\t<title>Tabela</title>\n",
    "\t<style>\n",
    "\t\tth,\n",
    "\t\ttd {\n",
    "\t\t\tborder: 2px solid blue;\n",
    "\t\t\tbackground-color: #eeeeff;\n",
    "\t\t}\n",
    "\t</style>\n",
    "</head>\n",
    "\n",
    "\n",
    "<body>\n",
    '\t<h1 style="text-align: center;">Tabela com Nomes</h1>\n',
    "\t<hr />\n",
    "\t<br />\n",
    "\n",
    "\n",
    '\t<table style="width:100%; margin:auto; border-collapse: collapse;">\n',
    "\n",
    "\t</table>\n",
    "\n",
    "\n",
    "</body>\n",
    "\n",
    "\n",
    "</html>\n",
]


lista = [
    "Colt McCoy QB, CLE\t135\t222\t1576\t6\t9\t60.8%\t74.5\n",
    "Josh Freeman QB, TB\t291\t474\t3451\t25\t6\t61.4%\t95.9\n",
    "Michael Vick QB, PHI\t233\t372\t3018\t21\t6\t62.6%\t100.2\n",
    "Matt Schaub QB, HOU\t365\t574\t4370\t24\t12\t63.6%\t92.0\n",
    "Philip Rivers QB, SD\t357\t541\t4710\t30\t13\t66.0%\t101.8\n",
    "Matt Hasselbeck QB, SEA\t266\t444\t3001\t12\t17\t59.9%\t73.2\n",
    "Jimmy Clausen QB, CAR\t157\t299\t1558\t3\t9\t52.5%\t58.4\n",
    "Joe Flacco QB, BAL\t306\t489\t3622\t25\t10\t62.6%\t93.6\n",
    "Kyle Orton QB, DEN\t293\t498\t3653\t20\t9\t58.8%\t87.5\n",
    "Jason Campbell QB, OAK\t194\t329\t2387\t13\t8\t59.0%\t84.5\n",
    "Peyton Manning QB, IND\t450\t679\t4700\t33\t17\t66.3%\t91.9\n",
    "Drew Brees QB, NO\t448\t658\t4620\t33\t22\t68.1%\t90.9\n",
    "Matt Ryan QB, ATL\t357\t571\t3705\t28\t9\t62.5%\t91.0\n",
    "Matt Cassel QB, KC\t262\t450\t3116\t27\t7\t58.2%\t93.0\n",
    "Mark Sanchez QB, NYJ\t278\t507\t3291\t17\t13\t54.8%\t75.3\n",
    "Brett Favre QB, MIN\t217\t358\t2509\t11\t19\t60.6%\t69.9\n",
    "David Garrard QB, JAC\t236\t366\t2734\t23\t15\t64.5%\t90.8\n",
    "Eli Manning QB, NYG\t339\t539\t4002\t31\t25\t62.9%\t85.3\n",
    "Carson Palmer QB, CIN\t362\t586\t3970\t26\t20\t61.8%\t82.4\n",
    "Alex Smith QB, SF\t204\t342\t2370\t14\t10\t59.6%\t82.1\n",
    "Chad Henne QB, MIA\t301\t490\t3301\t15\t19\t61.4%\t75.4\n",
    "Tony Romo QB, DAL\t148\t213\t1605\t11\t7\t69.5%\t94.9\n",
    "Jay Cutler QB, CHI\t261\t432\t3274\t23\t16\t60.4%\t86.3\n",
    "Jon Kitna QB, DAL\t209\t318\t2365\t16\t12\t65.7%\t88.9\n",
    "Tom Brady QB, NE\t324\t492\t3900\t36\t4\t65.9%\t111.0\n",
    "Ben Roethlisberger QB, PIT\t240\t389\t3200\t17\t5\t61.7%\t97.0\n",
    "Kerry Collins QB, TEN\t160\t278\t1823\t14\t8\t57.6%\t82.2\n",
    "Derek Anderson QB, ARI\t169\t327\t2065\t7\t10\t51.7%\t65.9\n",
    "Ryan Fitzpatrick QB, BUF\t255\t441\t3000\t23\t15\t57.8%\t81.8\n",
    "Donovan McNabb QB, WAS\t275\t472\t3377\t14\t15\t58.3%\t77.1\n",
    "Kevin Kolb QB, PHI\t115\t189\t1197\t7\t7\t60.8%\t76.1\n",
    "Aaron Rodgers QB, GB\t312\t475\t3922\t28\t11\t65.7%\t101.2\n",
    "Sam Bradford QB, STL\t354\t590\t3512\t18\t15\t60.0%\t76.5\n",
]


numero = 0
celula = ""


with open("qbdata.txt", "w") as arquivo:
    for linha in range(len(lista)):
        arquivo.writelines(lista[linha])


with open("qbdata.txt", "r") as file:
    lista = file.readlines()

    for i in range(len(lista)):
        valor = lista[i].split()
        nome = f"{valor[0]} {valor[1]}"
        numero += 1
        celula += (
            f"\t\t<tr>\n\t\t\t<th>{numero}</th>\n\t\t\t<th>{nome}</th>\n\t\t</tr>\n"
        )
        htmlLista[24] = celula

        with open("qbdata.html", "w") as htmlWrite:
            for linha in htmlLista:
                htmlWrite.write(linha)
