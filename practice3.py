# 다음 문장에서 “lorem”이 나오는 개수를 출력하는 프로그램을 작성하세요

sentence = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ornare nunc et orci aliquet hendrerit. Morbi mi
risus, ultrices a elit nec, mollis finibus eros. Mauris porta quis ante nec consectetur. Vestibulum in tempus
ipsum, nec malesuada ipsum. Vivamus aliquet lacus nec nisi commodo elementum. Morbi sed est a massa
dapibus efficitur. Praesent gravida massa at diam accumsan mattis. Cras viverra commodo dui at facilisis.
Maecenas vel ante et neque euismod ultrices. Duis ac justo odio. Nunc nec pretium nisi.
Suspendisse lectus metus, euismod id rhoncus quis, euismod eget elit. Sed luctus rutrum arcu, in suscipit
quam blandit eget. Curabitur sed enim tempor purus accumsan fringilla at nec tortor. Lorem ipsum dolor sit
amet, consectetur adipiscing elit. In eu massa urna. Morbi viverra ullamcorper odio aliquam tristique. Praesent
quis augue vestibulum, fermentum nunc vitae, pulvinar ex. Aenean eu suscipit metus. Fusce quis sollicitudin
tellus. Nunc maximus diam ac elit elementum, sed blandit lorem accumsan. Etiam non blandit ex. Etiam justo
libero, faucibus eget dolor vitae, pulvinar commodo sapien.
Nunc ut lorem semper, auctor augue vitae, volutpat nibh. Nulla ultricies iaculis sem, vel maximus augue
egestas et. Nunc suscipit nulla ut finibus pretium. Suspendisse elementum, urna quis bibendum ullamcorper,
urna lorem efficitur erat, id cursus orci eros sed ligula. Pellentesque placerat ut lacus vel mollis. Fusce non
risus sapien. Nam vel elementum velit. Aliquam lacinia, orci a tempus congue, justo sem eleifend ex, et gravida
diam est at purus. Nullam tincidunt, ipsum sed convallis hendrerit, massa urna porttitor turpis, id bibendum
diam nisi ut neque."""
a = sentence.lower()
print(a.count('lorem'))