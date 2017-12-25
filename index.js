[...document.getElementById('gene-tabular-docsum').querySelectorAll('tr')]
  .slice(1)
  .map(tr => tr.childNodes[2].textContent)
  .map(text => {
    if (!text) {
      return '';
    }
    const [rawId, rawLocations] = text.split('(');
    let gid = rawId.replace(/\s/g, '').split(',');
    gid = gid.length > 1 ? gid[1] : gid[0];
    gid = gid.replace(/\s/g, '');
    console.log(text.split('('), rawLocations);
    const [gcoors, strand] = rawLocations.split(',');
    const [from, to] = gcoors.replace(')', '').split('..');
    const link = `https://www.ncbi.nlm.nih.gov/nuccore/${gid}?report=fasta&from=${from}&to=${to}${
      strand ? '&strand=true' : ''
    }`;
    return link;
  })
  .filter(link => link.length)
  .join('\n');

document
  .getElementById('viewercontent1')
  .querySelector('pre')
  .innerText.replace(/^\s*\n/gm, '');
