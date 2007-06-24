# Copyright (C) 2006-2007 Red Hat, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import random

_colors = [
['#472E17', '#3A6E3A'], \
['#145435', '#997599'], \
['#C2B00C', '#3A333A'], \
['#0C4C70', '#C25EC2'], \
['#0CBDF0', '#113511'], \
['#5E4505', '#997599'], \
['#4519D7', '#576E57'], \
['#073838', '#47A147'], \
['#6E3D1E', '#EB73EB'], \
['#4519D7', '#7DB07D'], \
['#0C3A19', '#66A366'], \
['#610A45', '#E32BE3'], \
['#3A3307', '#AB91AB'], \
['#073838', '#35C235'], \
['#07571E', '#2E872E'], \
['#680211', '#F517F5'], \
['#35C2C0', '#E1E3E1'], \
['#F09C23', '#FDD9FD'], \
['#C29CFD', '#118511'], \
['#F391B3', '#B817B8'], \
['#4F0C73', '#C76EC7'], \
['#145435', '#23A823'], \
['#073838', '#4A424A'], \
['#F391B3', '#FDD9FD'], \
['#6E3D1E', '#118511'], \
['#680211', '#F3E1F3'], \
['#073838', '#356835'], \
['#2BC78C', '#0F8A0F'], \
['#94111C', '#C71EC7'], \
['#F391B3', '#91FA91'], \
['#472E17', '#AB3DAB'], \
['#610A45', '#216E21'], \
['#331194', '#356835'], \
['#331194', '#7DB07D'], \
['#0C4C70', '#C25EC2'], \
['#7017A3', '#EBDEEB'], \
['#073838', '#3A6E3A'], \
['#7DB0FA', '#61FA61'], \
['#F8975E', '#F517F5'], \
['#331194', '#785C78'], \
['#472E17', '#EB73EB'], \
['#5E4505', '#F517F5'], \
['#35C2C0', '#308C30'], \
['#680211', '#785C78'], \
['#7017A3', '#C76EC7'], \
['#7DB0FA', '#E1E3E1'], \
['#7017A3', '#F517F5'], \
['#0C3A19', '#75C275'], \
['#0CBDF0', '#C71EC7'], \
['#113547', '#266826'], \
['#0C3A19', '#97FA97'], \
['#4F0C73', '#EBDEEB'], \
['#F8975E', '#C217C2'], \
['#3A3307', '#216E21'], \
['#0C3A19', '#AB3DAB'], \
['#C29CFD', '#118511'], \
['#0C4C70', '#118511'], \
['#F8975E', '#680268'], \
['#C2B00C', '#5E455E'], \
['#680211', '#FDBAFD'], \
['#4F0C73', '#266826'], \
['#07571E', '#C71EC7'], \
['#C29CFD', '#D4E6D4'], \
['#0C3A19', '#AB3DAB'], \
['#073838', '#61FA61'], \
['#7DB0FA', '#576E57'], \
['#C29CFD', '#F517F5'], \
['#94111C', '#2E872E'], \
['#1C514F', '#2E872E'], \
['#680211', '#F863F8'], \
['#C2B00C', '#785C78'], \
['#C2B00C', '#576E57'], \
['#113547', '#D4E6D4'], \
['#07571E', '#75C275'], \
['#0C4C70', '#0F8A0F'], \
['#5E4505', '#F517F5'], \
['#94111C', '#F897F8'], \
['#680211', '#A114A1'], \
['#2BC78C', '#193819'], \
['#2BC78C', '#216E21'], \
['#331194', '#359735'], \
['#75C228', '#2E872E'], \
['#8F0C51', '#F8B8F8'], \
['#3A3307', '#C2B0C2'], \
['#7DB0FA', '#451945'], \
['#1C514F', '#61FA61'], \
['#7DB0FA', '#997599'], \
['#7017A3', '#308C30'], \
['#7DB0FA', '#61FA61'], \
['#2BC78C', '#118511'], \
['#C29CFD', '#C71EC7'], \
['#75C228', '#F3E3F3'], \
['#1C514F', '#47A147'], \
['#F391B3', '#91FA91'], \
['#193828', '#2BC72B'], \
['#145435', '#40E340'], \
['#331194', '#4A424A'], \
['#680211', '#F863F8'], \
['#5E4505', '#AB91AB'], \
['#5E4505', '#D1CFD1'], \
['#2BC78C', '#193819'], \
['#94111C', '#F3E1F3'], \
['#0C4C70', '#D4E6D4'], \
['#0C4C70', '#118511'], \
['#145435', '#91FA91'], \
['#07571E', '#308C30'], \
['#35C2C0', '#97FA97'], \
['#F8975E', '#F0EBF0'], \
['#6E3D1E', '#C25EC2'], \
['#472E17', '#3A6E3A'], \
['#C29CFD', '#F3E1F3'], \
['#F391B3', '#B817B8'], \
['#113547', '#266826'], \
['#113547', '#0CBD0C'], \
['#073838', '#35C235'], \
['#331194', '#576E57'], \
['#35C2C0', '#576E57'], \
['#1C514F', '#576E57'], \
['#75C228', '#308C30'], \
['#0CBDF0', '#C25EC2'], \
['#331194', '#AECCAE'], \
['#07571E', '#66A366'], \
['#C2B00C', '#785C78'], \
['#C29CFD', '#F517F5'], \
['#7017A3', '#EBDEEB'], \
['#F8975E', '#997599'], \
['#75C228', '#C71EC7'], \
['#1C514F', '#47A147'], \
['#F09C23', '#AB3DAB'], \
['#0C3A19', '#38E838'], \
['#75C228', '#3A6E3A'], \
['#7017A3', '#DEBADE'], \
['#1C514F', '#308C30'], \
['#3A3307', '#4A424A'], \
['#94111C', '#F517F5'], \
['#35C2C0', '#356835'], \
['#5E4505', '#C2B0C2'], \
['#C29CFD', '#A114A1'], \
['#C29CFD', '#A114A1'], \
['#4F0C73', '#3A6E3A'], \
['#3A3307', '#C2B0C2'], \
['#F391B3', '#610A61'], \
['#35C2C0', '#97FA97'], \
['#0CBDF0', '#0C4C0C'], \
['#8F0C51', '#0F8A0F'], \
['#1C514F', '#576E57'], \
['#6E3D1E', '#F09CF0'], \
['#5E4505', '#997599'], \
['#472E17', '#C25EC2'], \
['#4F0C73', '#A114A1'], \
['#680211', '#FDBAFD'], \
['#4F0C73', '#EBDEEB'], \
['#4519D7', '#E1E3E1'], \
['#610A45', '#B817B8'], \
['#C2B00C', '#91FA91'], \
['#8F0C51', '#E32BE3'], \
['#07571E', '#38E838'], \
['#2BC78C', '#FDD9FD'], \
['#610A45', '#AB3DAB'], \
['#472E17', '#EB73EB'], \
['#F391B3', '#FDD9FD'], \
['#0CBDF0', '#D4E6D4'], \
['#07571E', '#66A366'], \
['#C29CFD', '#308C30'], \
['#8F0C51', '#F85CF8'], \
['#F391B3', '#E1E3E1'], \
['#F8975E', '#997599'], \
['#6E3D1E', '#F09CF0'], \
['#2BC78C', '#997599'], \
['#4F0C73', '#C71EC7'], \
['#F391B3', '#C25EC2'], \
['#680211', '#356835'], \
['#0C4C70', '#0F8A0F'], \
['#610A45', '#4A424A'], \
['#35C2C0', '#F517F5'], \
['#07571E', '#75C275'], \
['#4519D7', '#E32BE3'], \
['#75C228', '#2E872E'], \
['#35C2C0', '#073807'], \
['#75C228', '#F3E3F3'], \
['#3A3307', '#C217C2'], \
['#35C2C0', '#1C511C'], \
['#C2B00C', '#F517F5'], \
['#7017A3', '#C71EC7'], \
['#C2B00C', '#0F8A0F'], \
['#113547', '#216E21'], \
['#4F0C73', '#DEBADE'], \
['#0CBDF0', '#C25EC2'], \
['#C2B00C', '#F0EBF0'], \
['#610A45', '#F8B8F8'], \
['#193828', '#216E21'], \
['#0C3A19', '#308C30'], \
['#073838', '#C217C2'], \
['#4519D7', '#2E872E'], \
['#331194', '#AECCAE'], \
['#0CBDF0', '#0F8A0F'], \
['#F09C23', '#472E47'], \
['#94111C', '#F3E1F3'], \
['#331194', '#356835'], \
['#1C514F', '#17E317'], \
['#75C228', '#075707'], \
['#6E3D1E', '#F8C2F8'], \
['#07571E', '#2E872E'], \
['#680211', '#A114A1'], \
['#C2B00C', '#F0EBF0'], \
['#113547', '#216E21'], \
['#8F0C51', '#576E57'], \
['#472E17', '#B817B8'], \
['#F09C23', '#D4E6D4'], \
['#073838', '#61FA61'], \
['#C2B00C', '#576E57'], \
['#145435', '#997599'], \
['#3A3307', '#997599'], \
['#193828', '#0F8A0F'], \
['#0C4C70', '#0CBD0C'], \
['#C2B00C', '#0F8A0F'], \
['#5E4505', '#0F8A0F'], \
['#C29CFD', '#97FA97'], \
['#F8975E', '#2E872E'], \
['#331194', '#4A424A'], \
['#1C514F', '#17E317'], \
['#680211', '#F897F8'], \
['#113547', '#A114A1'], \
['#073838', '#47A147'], \
['#F09C23', '#118511'], \
['#1C514F', '#F517F5'], \
['#75C228', '#97FA97'], \
['#0C4C70', '#D4E6D4'], \
['#3A3307', '#D1CFD1'], \
['#073838', '#C217C2'], \
['#75C228', '#61FA61'], \
['#35C2C0', '#2E872E'], \
['#F8975E', '#EBDEEB'], \
['#472E17', '#F09CF0'], \
['#35C2C0', '#F3E1F3'], \
['#193828', '#785C78'], \
['#193828', '#266826'], \
['#C29CFD', '#4F0C4F'], \
['#94111C', '#FDBAFD'], \
['#07571E', '#97FA97'], \
['#0CBDF0', '#C71EC7'], \
['#F8975E', '#61FA61'], \
['#472E17', '#C25EC2'], \
['#5E4505', '#0F8A0F'], \
['#C2B00C', '#997599'], \
['#0CBDF0', '#F3E3F3'], \
['#145435', '#118511'], \
['#6E3D1E', '#C25EC2'], \
['#1C514F', '#308C30'], \
['#3A3307', '#F0EBF0'], \
['#F09C23', '#F3E3F3'], \
['#610A45', '#FDD9FD'], \
['#145435', '#0F8A0F'], \
['#472E17', '#AB3DAB'], \
['#C29CFD', '#308C30'], \
['#0CBDF0', '#0F8A0F'], \
['#4519D7', '#576E57'], \
['#113547', '#118511'], \
['#2BC78C', '#118511'], \
['#F8975E', '#F517F5'], \
['#1C514F', '#2E872E'], \
['#4F0C73', '#C29CC2'], \
['#4F0C73', '#DEBADE'], \
['#5E4505', '#576E57'], \
['#F09C23', '#E32BE3'], \
['#0CBDF0', '#D4E6D4'], \
['#94111C', '#F863F8'], \
['#0C3A19', '#A114A1'], \
['#2BC78C', '#145414'], \
['#6E3D1E', '#E32BE3'], \
['#0CBDF0', '#118511'], \
['#35C2C0', '#308C30'], \
['#6E3D1E', '#F3E3F3'], \
['#6E3D1E', '#EB73EB'], \
['#7017A3', '#C29CC2'], \
['#7017A3', '#308C30'], \
['#C29CFD', '#701770'], \
['#F8975E', '#C71EC7'], \
['#331194', '#7DB07D'], \
['#113547', '#51DC51'], \
['#113547', '#3A9E3A'], \
['#610A45', '#E32BE3'], \
['#F09C23', '#308C30'], \
['#0C3A19', '#308C30'], \
['#610A45', '#B817B8'], \
['#145435', '#91FA91'], \
['#2BC78C', '#D4E6D4'], \
['#C2B00C', '#F517F5'], \
['#4519D7', '#E1E3E1'], \
['#680211', '#F3E1F3'], \
['#610A45', '#F85CF8'], \
['#6E3D1E', '#308C30'], \
['#145435', '#2BC72B'], \
['#7DB0FA', '#E1E3E1'], \
['#0C3A19', '#3A6E3A'], \
['#75C228', '#3A6E3A'], \
['#610A45', '#4A424A'], \
['#F391B3', '#0F8A0F'], \
['#145435', '#2BC72B'], \
['#7DB0FA', '#F0EBF0'], \
['#75C228', '#EBDEEB'], \
['#145435', '#E32BE3'], \
['#8F0C51', '#F85CF8'], \
['#472E17', '#266826'], \
['#94111C', '#FDBAFD'], \
['#F391B3', '#E32BE3'], \
['#073838', '#2E872E'], \
['#4F0C73', '#266826'], \
['#145435', '#23A823'], \
['#5E4505', '#D1CFD1'], \
['#C2B00C', '#E1E3E1'], \
['#145435', '#118511'], \
['#0C4C70', '#51DC51'], \
['#75C228', '#61FA61'], \
['#7DB0FA', '#331133'], \
['#F09C23', '#6E3D6E'], \
['#F09C23', '#C25EC2'], \
['#75C228', '#308C30'], \
['#193828', '#0F8A0F'], \
['#0C3A19', '#75C275'], \
['#C2B00C', '#F3E1F3'], \
['#94111C', '#F897F8'], \
['#2BC78C', '#91FA91'], \
['#3A3307', '#785C78'], \
['#610A45', '#F391F3'], \
['#193828', '#B817B8'], \
['#193828', '#216E21'], \
['#193828', '#B817B8'], \
['#7DB0FA', '#576E57'], \
['#7DB0FA', '#F0EBF0'], \
['#0C3A19', '#A114A1'], \
['#0C3A19', '#97FA97'], \
['#7017A3', '#118511'], \
['#680211', '#F517F5'], \
['#331194', '#785C78'], \
['#35C2C0', '#356835'], \
['#073838', '#2E872E'], \
['#3A3307', '#D1CFD1'], \
['#8F0C51', '#C25EC2'], \
['#35C2C0', '#576E57'], \
['#75C228', '#0C3A0C'], \
['#35C2C0', '#1C511C'], \
['#073838', '#4A424A'], \
['#F8975E', '#EBDEEB'], \
['#8F0C51', '#576E57'], \
['#35C2C0', '#2E872E'], \
['#94111C', '#F517F5'], \
['#0CBDF0', '#266826'], \
['#75C228', '#97FA97'], \
['#F8975E', '#F0EBF0'], \
['#113547', '#118511'], \
['#193828', '#266826'], \
['#0CBDF0', '#91FA91'], \
['#F8975E', '#F3E1F3'], \
['#680211', '#C217C2'], \
['#0C3A19', '#38E838'], \
['#4519D7', '#359735'], \
['#113547', '#AB3DAB'], \
['#0CBDF0', '#118511'], \
['#C29CFD', '#701770'], \
['#3A3307', '#785C78'], \
['#C29CFD', '#D4E6D4'], \
['#7DB0FA', '#E32BE3'], \
['#F8975E', '#C217C2'], \
['#94111C', '#C71EC7'], \
['#75C228', '#C71EC7'], \
['#145435', '#40E340'], \
['#F09C23', '#D4E6D4'], \
['#0C3A19', '#66A366'], \
['#113547', '#D4E6D4'], \
['#6E3D1E', '#E32BE3'], \
['#07571E', '#38E838'], \
['#145435', '#E32BE3'], \
['#0C3A19', '#356835'], \
['#7DB0FA', '#997599'], \
['#07571E', '#C25EC2'], \
['#C2B00C', '#E1E3E1'], \
['#0C4C70', '#3A9E3A'], \
['#7DB0FA', '#4A424A'], \
['#3A3307', '#AB91AB'], \
['#7DB0FA', '#4A424A'], \
['#F09C23', '#AB3DAB'], \
['#472E17', '#F3E3F3'], \
['#07571E', '#308C30'], \
['#F09C23', '#308C30'], \
['#610A45', '#F391F3'], \
['#4F0C73', '#3A6E3A'], \
['#C2B00C', '#5E455E'], \
['#4519D7', '#2E872E'], \
['#6E3D1E', '#F3E3F3'], \
['#8F0C51', '#F8B8F8'], \
['#94111C', '#2E872E'], \
['#C29CFD', '#97FA97'], \
['#F391B3', '#F3E3F3'], \
['#C2B00C', '#F3E1F3'], \
['#680211', '#F897F8'], \
['#C29CFD', '#EBDEEB'], \
['#7DB0FA', '#331133'], \
['#F09C23', '#FDD9FD'], \
['#4F0C73', '#C217C2'], \
['#610A45', '#F8B8F8'], \
['#7017A3', '#C76EC7'], \
['#F8975E', '#941194'], \
['#3A3307', '#F0EBF0'], \
['#193828', '#23A823'], \
['#2BC78C', '#145414'], \
['#75C228', '#0C3A0C'], \
['#610A45', '#216E21'], \
['#07571E', '#C71EC7'], \
['#2BC78C', '#0F8A0F'], \
['#113547', '#0CBD0C'], \
['#F09C23', '#97FA97'], \
['#F09C23', '#97FA97'], \
['#5E4505', '#C2B0C2'], \
['#07571E', '#C25EC2'], \
['#3A3307', '#4A424A'], \
['#7DB0FA', '#2E872E'], \
['#7DB0FA', '#FDD9FD'], \
['#472E17', '#B817B8'], \
['#4F0C73', '#C76EC7'], \
['#F391B3', '#E32BE3'], \
['#4F0C73', '#C29CC2'], \
['#472E17', '#F09CF0'], \
['#94111C', '#F863F8'], \
['#F391B3', '#E1E3E1'], \
['#331194', '#E1E3E1'], \
['#7017A3', '#118511'], \
['#145435', '#0F8A0F'], \
['#0C3A19', '#356835'], \
['#C29CFD', '#EBDEEB'], \
['#610A45', '#FDD9FD'], \
['#0C4C70', '#C71EC7'], \
['#07571E', '#97FA97'], \
['#4519D7', '#AECCAE'], \
['#F8975E', '#680268'], \
['#75C228', '#075707'], \
['#8F0C51', '#E32BE3'], \
['#0CBDF0', '#EBDEEB'], \
['#F09C23', '#F3E3F3'], \
['#C29CFD', '#C71EC7'], \
['#94111C', '#997599'], \
['#F391B3', '#0F8A0F'], \
['#35C2C0', '#61FA61'], \
['#193828', '#2BC72B'], \
['#1C514F', '#F517F5'], \
['#7017A3', '#DEBADE'], \
['#2BC78C', '#D4E6D4'], \
['#4519D7', '#7DB07D'], \
['#F391B3', '#8F0C8F'], \
['#5E4505', '#AB91AB'], \
['#8F0C51', '#F391F3'], \
['#680211', '#785C78'], \
['#F8975E', '#C71EC7'], \
['#0CBDF0', '#113511'], \
['#F391B3', '#F3E3F3'], \
['#2BC78C', '#E32BE3'], \
['#0CBDF0', '#0C4C0C'], \
['#073838', '#356835'], \
['#35C2C0', '#F517F5'], \
['#F391B3', '#610A61'], \
['#0C4C70', '#51DC51'], \
['#2BC78C', '#997599'], \
['#472E17', '#F3E3F3'], \
['#F8975E', '#61FA61'], \
['#2BC78C', '#91FA91'], \
['#F391B3', '#576E57'], \
['#94111C', '#997599'], \
['#1C514F', '#61FA61'], \
['#F09C23', '#6E3D6E'], \
['#75C228', '#C25EC2'], \
['#6E3D1E', '#F8C2F8'], \
['#4F0C73', '#C217C2'], \
['#F09C23', '#C25EC2'], \
['#0CBDF0', '#266826'], \
['#4F0C73', '#C71EC7'], \
['#35C2C0', '#61FA61'], \
['#193828', '#91FA91'], \
['#0CBDF0', '#EBDEEB'], \
['#6E3D1E', '#308C30'], \
['#C2B00C', '#91FA91'], \
['#5E4505', '#576E57'], \
['#C2B00C', '#3A333A'], \
['#F8975E', '#2E872E'], \
['#3A3307', '#216E21'], \
['#193828', '#91FA91'], \
['#073838', '#17E317'], \
['#35C2C0', '#E1E3E1'], \
['#331194', '#359735'], \
['#472E17', '#266826'], \
['#7DB0FA', '#2E872E'], \
['#113547', '#A114A1'], \
['#7017A3', '#F517F5'], \
['#C29CFD', '#F3E1F3'], \
['#0C4C70', '#C71EC7'], \
['#4519D7', '#997599'], \
['#0C4C70', '#0CBD0C'], \
['#680211', '#C217C2'], \
['#193828', '#40E340'], \
['#6E3D1E', '#118511'], \
['#0C4C70', '#3A9E3A'], \
['#193828', '#23A823'], \
['#5E4505', '#F0EBF0'], \
['#331194', '#B817B8'], \
['#7DB0FA', '#FDD9FD'], \
['#F09C23', '#118511'], \
['#113547', '#51DC51'], \
['#0CBDF0', '#91FA91'], \
['#F391B3', '#C25EC2'], \
['#331194', '#B817B8'], \
['#2BC78C', '#FDD9FD'], \
['#331194', '#576E57'], \
['#7DB0FA', '#E32BE3'], \
['#193828', '#40E340'], \
['#F391B3', '#576E57'], \
['#331194', '#E1E3E1'], \
['#472E17', '#F8C2F8'], \
['#3A3307', '#C217C2'], \
['#75C228', '#EBDEEB'], \
['#7017A3', '#C71EC7'], \
['#F09C23', '#E32BE3'], \
['#4519D7', '#E32BE3'], \
['#680211', '#356835'], \
['#35C2C0', '#F3E1F3'], \
['#1C514F', '#35C235'], \
['#8F0C51', '#F391F3'], \
['#113547', '#AB3DAB'], \
['#193828', '#785C78'], \
['#8F0C51', '#FDD9FD'], \
['#F09C23', '#472E47'], \
['#7DB0FA', '#451945'], \
['#2BC78C', '#F0EBF0'], \
['#113547', '#3A9E3A'], \
['#8F0C51', '#FDD9FD'], \
['#C2B00C', '#997599'], \
['#75C228', '#C25EC2'], \
['#4519D7', '#997599'], \
['#4519D7', '#AECCAE'], \
['#4F0C73', '#A114A1'], \
['#2BC78C', '#216E21'], \
['#7017A3', '#C29CC2'], \
['#472E17', '#F8C2F8'], \
['#610A45', '#AB3DAB'], \
['#0CBDF0', '#F3E3F3'], \
['#0C3A19', '#3A6E3A'], \
['#610A45', '#F85CF8'], \
['#073838', '#17E317'], \
['#35C2C0', '#073807'], \
['#2BC78C', '#E32BE3'], \
['#5E4505', '#F0EBF0'], \
['#C29CFD', '#4F0C4F'], \
['#F8975E', '#F3E1F3'], \
['#8F0C51', '#C25EC2'], \
['#F391B3', '#8F0C8F'], \
['#073838', '#3A6E3A'], \
['#3A3307', '#997599'], \
['#4519D7', '#359735'], \
['#2BC78C', '#F0EBF0'], \
['#F8975E', '#941194'], \
['#1C514F', '#35C235'], \
['#8F0C51', '#0F8A0F'], \
]

def _parse_string(color_string):
    if color_string == 'white':
        return ['#ffffff', '#414141']
    elif color_string == 'insensitive':
        return ['#ffffff', '#e2e2e2']

    splitted = color_string.split(',')
    if len(splitted) == 2:
        return [splitted[0], splitted[1]]
    else:
        return None

def is_valid(color_string):
    return (_parse_string(color_string) != None)

class XoColor:
    def __init__(self, color_string=None):
        if color_string == None or not is_valid(color_string):
            n = int(random.random() * (len(_colors) - 1))
            [self._stroke, self._fill] = _colors[n]
        else:
            [self._stroke, self._fill] = _parse_string(color_string)

    def get_stroke_color(self):
        return self._stroke

    def get_fill_color(self):
        return self._fill

    def to_string(self):
        return '%s,%s' % (self._stroke, self._fill)
