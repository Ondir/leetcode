def merge_the_tools(string, k):

    total_str = [string[i:i+k] for i in range(0, len(string), k)]
    for i in total_str:
        print(''.join(dict.fromkeys(i)))


if __name__ == '__main__':
    string = 'KYQYTWXTDQXWDLKIXNWIITFBLIHRNGDZGVYCRXVWNUVSFFACUXMCSTFFBNWQVBQCWOEPNBOAVJUCOUGITSMNLSUOFRFAUXETNIKAJYCEJWIXSOHMGUBTOWKVPPXJOCEBKPDWNFCXDLWVZEJIALBOJLLYCIJQKOTXDWTSDVRIGOEIUPQUCRKLFVLHFXASNVPSUKKXHCGOSMYMDOIGHUTMPHWWEYORTFJNPVNXZVNTJNFMBPSIJOXAVTXZRNSKTDAKANJAKYTTLBFMSAXCOUCJNBKGPESKHSWJHGJREFKSISGASDCIZHTOKFUBJNLSFIBPQNGWSROCLVCDAHNAQGOALJCUYPOFZPUPEDMYWAAHXDKAMXACFQCQBGMZWAHVRBNYEZWABXJBCVBOSDQZTSPVZDWXFDSZHFXNGTQISZLUVMKPPAPIVGFWKCTRHNQQVPEBJULDVYAQKKGBLXMIDREPVZHFMZVJPZNAVADRZDHJOPNBMZLSQRHOQQTEQQOFSDFNDKGCOQOEFBHUASMSJTIBMDFCUVHOYOBCYKGOAWSHXBDZTPUELEFXINZEIISJYVNWFTNHQHPPJSREKNJXRQUZDVDOFVZDRMBYHOGZYXRHRILBVWYMPUOURRIWPJBIVFGFVOGTLXADHOGCMHRBDFWVYGTPQVXNCGUXUBRGYTLGJRKWADZEIVZJEUAURAJTGERCFIKFDVLNPWJPZITKGUVKPVGGXPADVTGCBQIGOTTDREUTPQFVKCFBZNKXEMAAFICIBMOPGKUZOQUDGZYTDFUDUGAZUCBZNFJQSAFAKBBYRWEYXETBMPEGWGHQKISZOBPIDWINXJORHSRFWKGIZMRXSYOEHIEXLTHPQPCPASGIMXPJJVTJHMGBLWHUELTQHAHZRJOTEXDQWSBGNXPWJXXWUHQASJSBLZCCJRWPQZFMUHSHEJEPHDMDKCDFOWIZVLEGECVUDDIXKDFQMLFVQRYDWEKMCSNZFRGJTDFZGOWSTBIFOOBHHBKDHUPJMDJSWRDSUJRDZNVSRGZHUCODGYHNUYXJDIDCZGUVRNYSAWMTCMDYORBWSKKMJJVORYQSHMNAZOTCKFVORAMISNEKAQYLZUZSUSKDEYEEMXGYEDMYEYGYNMKNDIYEEAXBSHEYHICVHKTMQHKUFSUVGEKJMLQTNNUFWYDEJIBQSVCIEOEMGAHNETYTEOMRDGYAEEGNMJGGEIRLZVXFYEUCXTVEJJXNPWPWAXLMGRUNCLYBHVIFBDJAYHGHQEWGANECMPQTJKILWIOFFWMIBVIZCPJVVHDVVHXJYPEHZMUVUKABJMJKISMMJVHGCKBZTAJSPPBOCYMYIMARZLEJFQXQNHWPRZRNBCFQRIHVGVURHWKIJOTPGRFTYCLRBEGDGLVZWEVEZRVJPIRYWLNFETAEVLXYPEBXRZXNDSSDLPMAXFYWSMBYHBCCPACGGEEXDDLIXFNIUBISHGOBURABSCFJEIQKOWITZVBWCPEWQOQZUEBRXBSQFYBKGRWUNENMBQKDFQCYESXZZYQWBKOHIQRQHNMXUBLXSWDZMFXRXVSYVKVZULGFBZXLOKKKNVIFTLFISEBPBTQZFNYBYEIADGNTSXEFSMLOZSWRYXIASYZXLXAMDJMIRBBJYHQSTDGUXENWBWYTWXSKWVWBGKJXLMILUADPEMKBQZZSVXNUWIESDCVJMEIZTSKNSPEYBOAUQBOLZBFVLLQONLZBQJALDMYWCCWFTYZJAPWZTEUERKVFWWIOGJZJVZHZDEHWCGHCYGDRKYVBKSIIPRYVCZGZYOZCUGAYOKDMQGFCGDFTVQBKHAHLBOKAELEARGYISDWIKCMSFULCKPNRRUCSKOUOAYQTHRBZUAKGCWZJQMLCBATSVXNHOHYOGOHPFLOALYGPXHAPUNSVONQLNDSBKQPSHYHMLYOYWXNTEPLYDDWRQMCDRWGDNXWWWFIJDXICWXXANIZQNXJEJNJCJQFYNDULLFXOEFSACQAPYBHMYQSJDDLPVTNLWKWHPTYTAQVDGVUHZCVZUNJYQWPOPEZMOXVFTTATKVWSTTBUVWTPJCPCZGQQLPEZOAHHVJBHFZAASBUPYNHJSWNTFFJQWORLQYSLITTPVTRNWLFWAMISKVLPBXFXNXKDXDOHYHYTCPJBAOXBAFVKDJCEIHDVGOYGTONRYMLCDUDEKDHKICWLNYRVIXQONQWGHMZFAMHDGNHSQQCYVBMIZFGJEYARPWZYIZDILMMUZVMPORQJSCTTJZDOYDHPZHPKGSURGINGGAXURNFLRYEDAJRAMYROFGYNAUHGDUOJUMFNBKYTIFWIOPKDPBRVHRIJLPQQMGBISGWWQWPZDNJSEWXTXOQHHZQUQILEPONJVJFLHWMLLYFPUEJTSZCBATXTDIXSZMEUVJFFGUSTSZJODUHXVKYYFVRIGQDFDHBASIHACZUWYDMDZUAUGYUNWLXEEALJJMLEUVEZUYVVDIYEEBZMBTZXHWDNZOYKALOXGTWDTTYZDYDHZETBAUAHTEWUSWEVHVSOQQRLJRKNPOWRSSSSMSBHYZBRVIODDGTVYMGHDRWUHTLZLFUZYXHYXKPUSFXXNSSLEZVJSREZMRAZXWZXUIVTSNNLSNIGFDRMEOVWGZXUTZUQYVNUDINXVCIOPTWXYNJCCGAKIZGBAARYVGUAOJYMMICDDYCBNNFRUFDCGKFHKYHIECKSNIGBTIFYIJAWXHPTPTXVFCERAMBEQMYDWFFPPMQYXQWUZLNOGMKLOOFQCGUSSVYPAFGPTWPQOLNOZACFPOTDDYWFEQAZNYQPFWFYVWOLIDBHGGOVUHYZHUHONHNCHDSOBZMYVCKFGNMMTBHOKHPSEWITFVXMAPABOOCMTORBBGNVHWLTFANLXVGCQERSTTWKIYWDMPENVTKCRVYWWLKVHQXZUQSQKQAUOYXCNDRJWCNNZNLXZVSIOSJIIDASTCOJANLQQFBMJQBIENGDIANWSWHBAJVVMMFOZSEQXHEIYGRCTZHDZUCSSLVUUSQGEVXEPBWNJAVJGOLZPSFPOJJIUGDOYTXFQUJFXFUIFSROIENYYUPMDYXXEAOEVNJLJUSGZPRHHIVPPKPNFECKCZKIZYPWNYJWTBEUQXDZIYRXLGKSLMCPLMAMMPIBPRXKVEFNDINLJGIUMTMZHQRVDTHRISTZJSKEWRUABHNKNWEBRSDAJWVOPDFZVYYGTKNRBHRDOHPDDUGWOJWZHSNWXTVSTWAMGNGKUXNKECPJYWHPHEOPYCLVXJPSFRHNFNZBMOMTTBERZMIJSXYQBLNYWESDVZRAOSCBHQUATYTTMCCEZCWCPJAMPUPLUINIBRLKJHKDIDYUFCZGEXIVJKHYFZLBJZJMSXWCEGFMMDHRHIALFIIOVSPARABCBMRULPWQYDCKILDPVDCDOKTLCILVJOAMCRGOGEGEHKQRYUGTZIWNVSYZALVLBXYGOGWWLCDUOTMMPUGPFEEAWFZZSWKUTKCJRYGECLYQGMFWHLNORRQQWRPROBLJMPTFPBJROHJUWOSFBFTTXJLVAAMQDZCPOVWFYFWOPIILWBQAILVFWGDWIPPLRRDFOZLOHJCWTMJSPBSYMNDIVGGDYXQPOTWEVJSCVWYOJHGYKYWWNCGIKONIMEXCZWJUFBWAAWPJFXJPWGLLKTUUIJFWPCAPAJJGNIINEXWMVFBTNPEXIAUSMZQBDRQEACMNKUAQSYCPGGKTVOTFRPYDOQERHXXKZJXLEABYAGNGMXCJNVOEKOJAFQTMNRWMCWXGYAEYITFWSHFIEWOQKYQPOJEBCAPFYOLYOSXZNEVINDQTZGJJGZBUKFXNHOSGCFGTZDSPJPZYURRTXAFEBGAOLABSOVATCHMEMGTYVSWSJOLIQQMSWPGJPJCDGEWILKMAQHYOBUGMITVBMJTIYBUNKYTQCRAQCPQUWOKYIQKTMHUYRPIPSCFEAYUDRWTTLJQIZAIJTUEFEAFVPNMHQTNSRJVLGQERBWBAXLKQIQXMRCJGPVQHPDAINXTVOAMPWQSVDENLUKXLOGUGEMNVRPFENBBDBQUZGMVJQIXNVUYJDURHGHEYWJELKGOLWJNEXIPQSMDPJDBMYSVGZZGYILJVTYGRJVXGFOWYBBNMFOAFHVLIWSGGFSBASKRBFOJLCGLFJYTOPTTYQHGMBPTGHWIZGZCMPLZTTKBDKUTZQPXGWGVZXQHEMPFTOHHFUGYOSBTCYMCOBBUZHRYEHFKUURPKYWRVESJWTEYRQCFSECTNVSUDXEZUWQGWOYRSQCQLGQFZTKTZOMMKEIPEPQANGGLUGDOYHEMQURPPDIOSUDEBNVFCLFPTNBNWGBUPHGFBXWTDGHVBMBEAYJEJQUCFXRBFSYUZGCCGYVJFFGIRJMTHXYSPUUWTNAYFAUGGWKOVGZCNFMGOAAXXAPOULKPYKNDKHLTGWJDEJFRQTXFTZESZUGVFSKEFZJRJXMPTWSZFZSVSPCNRHFQDNOIFAOMCYELVQCQOWRTVJRPAVCRCJKHWAQDAEQEEWPBMRTDNKYKVPBYLDPPMBXKDPOGVEKAAADOTXRJJQTHHXFSAWIPYHZBWNJRTUTTUZKPWDYHTUODRVVTSFKSOKVKZFEVZXQVWAKUELEZHUCYQATKHECWQXGRCMMDMDYKDJFJWLLDHNDXPWJXCLTSLBKNOYRABRKHARSWCDBMRELIBVFDGYYRAKHOIAQMRATUSNSWRUIKYUSBPYFXWFRYPYOXAEJTFENZSGVJCGVCCNETLLSKQJKFJZEJDQDKUSJOAHXCPUHRILMVWEHOOSVZRZLWRQHMIQALZAPOWWHEHTAFYJVOBQNUSARJQYXBQAMQCBGYYODHHFPHQKXSBLMVNFGEFEFYETQIUWGUMLEUSTDJFBDIORDBXKHEQMCWHSEEPKYBYEXSZDBFEENUWTVVDFZTTEPBWVFNHFRFKQYJTBQZIETGXRBCWCXPGOSFJXUQDLWPEWAXXRZFVUNUNOWLTTBBHTIQTDIYOGNUCNUCETJBNXVDNTOIORKXLSPGVYEMETGJGANNVYQLXOOLJCTYUFVHALPVJTJPMSYUULJQMCDJQRUZVQZRXVAXIPVRIEGWYHTTUELGGQQYJMAEEZWCUWZCOUVWBEVZNQUHUHOBXGBGSBNZBLBXJACXXZUYDRZQHUABDQEBWGHQHUPKFSIPVMOSLKSRBRJINJMRZSSXYBQIYHUFACWVQLPCVHVZYEHMOVDPOXPOAFYYOTGOXCLOPASLHNKIRTUHRZZHYQXYVWZLPFAMHNCZOUKXJWFDRZKKALRYBPXYLYKCDMQMZTLPPXNZVUENWQXWCRXFGWETUQVXCLLDGXVYWKZSEDHATGZXXWDFSHYOXVNBJYGPXBPULOOQTVSNDRKBNPIHWHXVCKYLJFDIGUCULQKENCTRWGULVCVULSRQFQDQVGYDDDXOTJUJOOCMWYXRASNONFESVHISQIXTLXJHIDQWTUKPSIHUCWIPBMJYWTSMCQHNPQUXTMWNGGCAQLVTIFKLUUKQNCERULFLBBJWOHLWPQXGDUBNZLZVHLLXPROMCTXFXIELPPJHHINLEQAGBZBLMPICGWOJSLQPUUCLKLSTWHGAXHGZIIKVZUXFQNOKAHZUBDINRAHNINNFWWGFGSAFMZKFMBPMIRJLURZLTGYDVOLSMRXUMZZAYLFMOXAYOLKKEJWYRWDOMOIAIHUUGVWGHCUXBXWPIIZNTXNMWQAIFLJNSDJBZFJIJEFKBDBJNDYGALSWEVHJGSYAXJBYQNGAROMUTQFHTEPVRISVFBGNTEPQPTPGGXIXNWTHMYQFEFBWPVTWYAJRGZHWSYEYWMXLIQSXQKCVQFTFAMCAMNRVOBRIBXIZJFLTXDQQOVLGAENDQRDFFXAVYTEZQMZBUKWTPPJFKULMAZPTQVYXSATSTZRLLSOHEKBUZMBLHNYJOPCGKAGECBWXAQILIYVPJYJKKKWRZWDNLFWYICCKDBIDRSQBRNQCLBMWMKPNISDUYZUGDWSIZANQVFSMTKQEMEAAPQNZKQTIRPQWOJENJREGXYSQIIWUNXUEPIDBAZKUOCQCLXSXOWDNUYDEICZVBVBQFHTGIDCYGSDTRVQGRUTNSZRCBSYCQBUVKNDSTFRBAUURPNZIJVVDUOFXJFZZHVWRKAMFHDGJZDBOQCWZXTCRJHQUNRTWMSPZSBEZELLFQOTGQRHOMJHYSYSFPOBEGRDYUJZBUKGMYCSRVZFIKOIDOAKEOOKUFPUBYWCVIJHJLCAGBHQOVYRKBDQPRCMYRIAPGCKPLUYYWAFZHXNEYGQZKGQBIEABNARTEDKQXKQTKXTRVIYTPOUZXKCHPCJEEAZJFKBFURYHPTAMCYHTNBSKNUREZAKFCKOKWRPSLPBAJCONAVGNYAZLWTSVVCDAORKMLZHWQIYBKMOLHWAHYCUVVMSQRVQFPCUADBYUJWVUIMFRKHYJJUGEHAXAWPFNSZPVANRKJNGTBNMNUMWEGEKPFHPDXVQRWFMZUELFTRYWEKJAWGGCMRURAJUZGKQDRFELLPQEIQCOALQYTXDGQXXQGSSNEKSYRYLCPCIXUKNXWDVPCAXSXVLGPDVVPPTHNFJCJUBDEOACTYSWYPQYMBEDGZZWQSDDZOHKIIONYQRROLPNDGNPHRTQSUMIMRNOFUYQCOFCFWVVILKLTXACOVSIPEQEXFSDZSVDHAFOWBJEOURHRULGPEQHKHLIOFNOZITGIZUECGLSACBRWMZOQQVBZGJNNWDMGXVOYRUCXFUXKXRGJQUAIRDJZOZMMEBSDWGBNAFLIBKSYBYIUVKCMNOODNAPRDHVBPYPPECXHMPIOQQKNCMBRAPUPSLHVSEXHCOYISYSGPAWFQGUUTWLVNHLFSUDM'
    k = 3452
    merge_the_tools(string, k)