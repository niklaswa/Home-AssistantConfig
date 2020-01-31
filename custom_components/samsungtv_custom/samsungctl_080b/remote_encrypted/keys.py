import binascii

publicKey = (
    '2cb12bb2cbf7cec713c0fff7b59ae68a96784ae517f41d259a45d20556177c0ffe951ca60'
    'ec03a990c9412619d1bee30adc7773088c5721664cffcedacf6d251cb4b76e2fd7aef09b3'
    'ae9f9496ac8d94ed2b262eee37291c8b237e880cc7c021fb1be0881f3d0bffa4234d3b8e6'
    'a61530c00473ce169c025f47fcc001d9b8051'
)
privateKey = (
    '2fd6334713816fae018cdee4656c5033a8d6b00e8eaea07b3624999242e96247112dcd019'
    'c4191f4643c3ce1605002b2e506e7f1d1ef8d9b8044e46d37c0d5263216a87cd783aa1854'
    '90436c4a0cb2c524e15bc1bfeae703bcbc4b74a0540202e8d79cadaae85c6f9c218bc1107'
    'd1f5b4b9bd87160e782f4e436eeb17485ab4d'
)
transKey = '6c9474469ddf7578f3e5ad8a4c703d99'
wbKey = 'abbb120c09e7114243d1fa0102163b27'
prime = (
    'b361eb0ab01c3439f2c16ffda7b05e3e320701ebee3e249123c3586765fd5bf6c1dfa88bb'
    '6bb5da3fde74737cd88b6a26c5ca31d81d18e3515533d08df619317063224cf0943a2f29a'
    '5fe60c1c31ddf28334ed76a6478a1122fb24c4a94c8711617ddfe90cf02e643cd82d4748d'
    '6d4a7ca2f47d88563aa2baf6482e124acd7dd'
)


BN_PRIME = int(prime, 16)
BN_PRIVATE_KEY = int(privateKey, 16)
PUBLIC_KEY = binascii.unhexlify(publicKey)
TRANS_KEY = binascii.unhexlify(transKey)
