import assert from "node:assert";

const expect = {
  md5: "4b3d106f3ad0a30205d5226e366330c0",
  sha1: "8fc336a0ab3783a220bf720686c6cea88a4f5bb4",
  sha224: "ffd93180daef705c12e62c8af8b035dab23e3019791d8c1c67c533b3",
  sha256: "d6bf020ca6a4afc19f6efe05c81db8b3e902c0f446bdac5d8808ef81ad16ca58",
  sha384: "f3d0ed57bddd5691cb7fd4ab80b963a9a6f4ee45e8917a3f03ec29b0098137e6ad1b44b8d959a4ea98edb047ac76d320",
  sha512: "9c8f99e1cd37c5e3024f3d108b8b89c3e32e6a287e709432d68cfde880ff4f53ee1d7cb4cf04bb265e4670c22d1f6bd9243d4a238b3332b72263320f2ef6d578",
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
