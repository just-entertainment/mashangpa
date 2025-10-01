const cry=require('crypto-js')

dd={
    a:cry
}
let key = dd['a']["enc"]["Utf8"]["parse"]("jo8j9wGw%6HbxfFn"),
    iv = dd['a']["enc"]['Utf8']["parse"]('0123456789ABCDEF');


function encrypt(jsonString) {
    // const _0x4d843e = _0x38addf;
    let _0x2703a2 = dd['a']['enc']['Utf8']['parse'](jsonString),
        _0x50fcf0 = dd['a']['AES']["encrypt"](_0x2703a2, key, {
            'mode': dd['a']['mode']['CBC'],
            'padding': dd['a']['pad']['Pkcs7'],
            'iv': iv
        });
    return _0x50fcf0['ciphertext']["toString"](cry["enc"]["Hex"]);
}


function loadPage(pageNumber) {
    // var csrfTokenInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
    const timestamp = new Date().getTime();
    const params = {
        page: pageNumber,
        _ts: timestamp,
    };
    const jsonString = JSON.stringify(params);
    let encryptedQuery = encrypt(jsonString);
    return {xl: encryptedQuery}
    // fetch(`/api/problem-detail/${problemId}/data/`, {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify({xl: encryptedQuery})
    // })
    //     .then(response => response.json())
    //     .then(data => updatePageContent(data))
    //     .catch(error => console.error('Error fetching problem details:', error));
}


// // "{"page":1,"_ts":1758638977322}"
// jsonString={"page":1,"_ts":1758638977322}
// console.log(encrypt(jsonString))
console.log(loadPage(1))
