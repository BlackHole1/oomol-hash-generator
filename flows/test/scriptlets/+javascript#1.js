import assert from "node:assert";

const expect = {
  md5: "4B3D106F3AD0A30205D5226E366330C0",
  sha1: "8FC336A0AB3783A220BF720686C6CEA88A4F5BB4",
  sha224: "FFD93180DAEF705C12E62C8AF8B035DAB23E3019791D8C1C67C533B3",
  sha256: "D6BF020CA6A4AFC19F6EFE05C81DB8B3E902C0F446BDAC5D8808EF81AD16CA58",
  sha384: "F3D0ED57BDDD5691CB7FD4AB80B963A9A6F4EE45E8917A3F03EC29B0098137E6AD1B44B8D959A4EA98EDB047AC76D320",
  sha512: "9C8F99E1CD37C5E3024F3D108B8B89C3E32E6A287E709432D68CFDE880FF4F53EE1D7CB4CF04BB265E4670C22D1F6BD9243D4A238B3332B72263320F2EF6D578",
}

export default async function(params, context) {
  assert(params.md5 === expect.md5, "md5 hash is not correct");
  assert(params.sha1 === expect.sha1, "sha1 hash is not correct");
  assert(params.sha224 === expect.sha224, "sha224 hash is not correct");
  assert(params.sha256 === expect.sha256, "sha256 hash is not correct");
  assert(params.sha384 === expect.sha384, "sha384 hash is not correct");
  assert(params.sha512 === expect.sha512, "sha512 hash is not correct");

  return {};
}
