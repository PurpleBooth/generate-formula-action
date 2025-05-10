# Changelog
All notable changes to this project will be documented in this file. See [conventional commits](https://www.conventionalcommits.org/) for commit guidelines.

- - -
## [v0.1.16](https://github.com/PurpleBooth/generate-formula-action/compare/e5faf652da175543fda9dbab09c784b95e4a32b8..v0.1.16) - 2025-05-10
#### Bug Fixes
- Add __init__.py to resolve mypy module duplication error - ([e5d88f1](https://github.com/PurpleBooth/generate-formula-action/commit/e5d88f1ca47b0c27a67208cf6d80be558b124562)) - Billie Thompson (aider)
- Add __init__.py to resolve mypy module resolution error - ([f61b7f5](https://github.com/PurpleBooth/generate-formula-action/commit/f61b7f56be1f5b798df21763d6fe901f8ec5d9cf)) - Billie Thompson (aider)
#### Continuous Integration
- Install mypy in GitHub Actions workflow - ([7e9a085](https://github.com/PurpleBooth/generate-formula-action/commit/7e9a085216a10813d1ba2f608e94f995c81acbf7)) - Billie Thompson (aider)
#### Miscellaneous Chores
- **(deps)** update cuchi/jinja2-action action to v1.3.0 - ([e5faf65](https://github.com/PurpleBooth/generate-formula-action/commit/e5faf652da175543fda9dbab09c784b95e4a32b8)) - renovate[bot]
- Make Jinja2 installation optional in action.yml - ([ee2d2c8](https://github.com/PurpleBooth/generate-formula-action/commit/ee2d2c8c76f1c2a172d053b5f493145be96fa9c9)) - Billie Thompson
- Update .gitignore and remove mypy from pip install in action.yml - ([035cac6](https://github.com/PurpleBooth/generate-formula-action/commit/035cac6f4c564e95ea790fe0fc3a2b1ab3c33f03)) - Billie Thompson
- Update Jinja2 action comment for template processing - ([2c1558e](https://github.com/PurpleBooth/generate-formula-action/commit/2c1558e372b733472ce091c701f7d6848e3d6978)) - Billie Thompson
#### Refactoring
- replace jinja2-action with direct Python script execution - ([5e352f2](https://github.com/PurpleBooth/generate-formula-action/commit/5e352f23b63fe1f6146a6362b9183a51482fcda6)) - Billie Thompson (aider)

- - -

## [v0.1.15](https://github.com/PurpleBooth/generate-formula-action/compare/af60cd399f09a611b3403a1debc37fe152da66b3..v0.1.15) - 2025-05-10
#### Bug Fixes
- roll back to older version that isn't broken - ([09e2138](https://github.com/PurpleBooth/generate-formula-action/commit/09e2138abd4b97a30105dc46371b9b1aab601760)) - Billie Thompson
#### Miscellaneous Chores
- **(deps)** update crazy-max/ghaction-import-gpg digest to e89d409 (#80) - ([bea8a90](https://github.com/PurpleBooth/generate-formula-action/commit/bea8a90a19145d28eb44069bd1ec0fb91d35beb8)) - renovate[bot]
- **(deps)** update ncipollo/release-action action to v1.16.0 (#79) - ([81e5b72](https://github.com/PurpleBooth/generate-formula-action/commit/81e5b721afb888e7066d40f99c2b701aaed1d418)) - renovate[bot]
- **(deps)** update cuchi/jinja2-action action to v1.3.0 (#78) - ([ae94223](https://github.com/PurpleBooth/generate-formula-action/commit/ae9422327c42a2942ae05febd030ddbefd2a7d5e)) - renovate[bot]
- **(deps)** update ncipollo/release-action action to v1.15.0 (#77) - ([a7a7944](https://github.com/PurpleBooth/generate-formula-action/commit/a7a794412fde46d34d6eb97a9f1bc307279080f4)) - renovate[bot]
- **(deps)** update crazy-max/ghaction-import-gpg digest to cb9bde2 - ([cba49a8](https://github.com/PurpleBooth/generate-formula-action/commit/cba49a8d6ff5fa55e940f8276b11491cb3a3ccb0)) - renovate[bot]
- **(deps)** update actions/checkout digest to 11bd719 - ([09fed71](https://github.com/PurpleBooth/generate-formula-action/commit/09fed71d893b6e49a18c96b43fa3c724543b15c3)) - renovate[bot]
- **(deps)** update actions/checkout digest to eef6144 - ([1d649e3](https://github.com/PurpleBooth/generate-formula-action/commit/1d649e302d5d8daeb5eef88090927e835e624ebc)) - renovate[bot]
- **(deps)** update purplebooth/changelog-action action to v0.3.4 - ([af60cd3](https://github.com/PurpleBooth/generate-formula-action/commit/af60cd399f09a611b3403a1debc37fe152da66b3)) - renovate[bot]

- - -

## [v0.1.14](https://github.com/PurpleBooth/generate-formula-action/compare/b0df6230c3d9de6536a6bfae12c2a79908cca1b4..v0.1.14) - 2024-08-20
#### Bug Fixes
- remove duplicated $ - ([70315e1](https://github.com/PurpleBooth/generate-formula-action/commit/70315e14cfbe3cba12297df7340bfe1349aea384)) - Billie Thompson
#### Continuous Integration
- Use cog to generate changelog - ([7bebb08](https://github.com/PurpleBooth/generate-formula-action/commit/7bebb08fc466f5ea26515c6cd266100c70e2fe70)) - Billie Thompson
- Remove mergify - ([b0df623](https://github.com/PurpleBooth/generate-formula-action/commit/b0df6230c3d9de6536a6bfae12c2a79908cca1b4)) - Billie Thompson
#### Miscellaneous Chores
- **(deps)** update crazy-max/ghaction-import-gpg action to v6 - ([a41062e](https://github.com/PurpleBooth/generate-formula-action/commit/a41062e824aefd4c33b0321d27a9136cf965dbfe)) - renovate[bot]
- **(deps)** update actions/checkout action to v4 - ([36258c8](https://github.com/PurpleBooth/generate-formula-action/commit/36258c81d1109d39bd78c634679ec998f6237c24)) - renovate[bot]
- **(deps)** update ncipollo/release-action action to v1.14.0 - ([145c814](https://github.com/PurpleBooth/generate-formula-action/commit/145c814e12fa78d5f2fe53424e94629578acfbc2)) - renovate[bot]
- **(deps)** update cuchi/jinja2-action action to v1.2.2 - ([b9738e0](https://github.com/PurpleBooth/generate-formula-action/commit/b9738e0b8a29f8e4f8eae475022781d299183334)) - renovate[bot]
- **(deps)** pin dependencies - ([fed4389](https://github.com/PurpleBooth/generate-formula-action/commit/fed4389ded6de95730a5e27cd1f7885ee1f7254f)) - renovate[bot]

- - -

## [v0.1.13](https://github.com/PurpleBooth/generate-formula-action/compare/86c27ee5d248b4f3d6d3dd43fe183eaf0bb06148..v0.1.13) - 2024-08-01
#### Bug Fixes
- Ignore creation failure - ([86c27ee](https://github.com/PurpleBooth/generate-formula-action/commit/86c27ee5d248b4f3d6d3dd43fe183eaf0bb06148)) - Billie Thompson

- - -

## [v0.1.12](https://github.com/PurpleBooth/generate-formula-action/compare/dc8ddc7a5380649a042920c83e5d4e12302da0c0..v0.1.12) - 2024-08-01
#### Bug Fixes
- Allow force pushing to enable runs - ([915dfc3](https://github.com/PurpleBooth/generate-formula-action/commit/915dfc3c72616ce992043760526c598a00e42414)) - Billie Thompson
- Use new format for output - ([c2c0168](https://github.com/PurpleBooth/generate-formula-action/commit/c2c0168b81755187660c439bd5a400e80087ba69)) - Billie Thompson
- bump crazy-max/ghaction-import-gpg from 4 to 5 - ([83ecd8d](https://github.com/PurpleBooth/generate-formula-action/commit/83ecd8dc37b5b714e6b7561694e4c8d5ebd9d39d)) - dependabot[bot]
- bump PurpleBooth/changelog-action from 0.3.2 to 0.3.3 - ([11485a1](https://github.com/PurpleBooth/generate-formula-action/commit/11485a13abf1965f8f5b4444da14d00ed92ca5e1)) - dependabot[bot]
- bump PurpleBooth/versio-release-action from 0.1.10 to 0.1.13 - ([1ca2112](https://github.com/PurpleBooth/generate-formula-action/commit/1ca2112fe16a5cd237baa0fb3fedbbe4075500c2)) - dependabot[bot]
- bump PurpleBooth/versio-release-action from 0.1.9 to 0.1.10 - ([fc4451b](https://github.com/PurpleBooth/generate-formula-action/commit/fc4451b24a1ee51e29c3514eac97d0c8df078da3)) - dependabot[bot]
- bump PurpleBooth/changelog-action from 0.1.1 to 0.3.2 - ([508907a](https://github.com/PurpleBooth/generate-formula-action/commit/508907a9b5f4292fc95dc633042bf414f603722d)) - dependabot[bot]
- bump actions/checkout from 2.3.5 to 3 - ([0a2b1a0](https://github.com/PurpleBooth/generate-formula-action/commit/0a2b1a09f0eabd5d6b48f24920bd69fc4250b938)) - dependabot[bot]
- bump PurpleBooth/versio-release-action from 0.1.8 to 0.1.9 - ([662768c](https://github.com/PurpleBooth/generate-formula-action/commit/662768c87b57826d4bbaa1df9a0ff3f14bb83687)) - dependabot[bot]
- bump PurpleBooth/changelog-action from 0.3.1 to 0.3.2 - ([4d13b99](https://github.com/PurpleBooth/generate-formula-action/commit/4d13b995dc7c0c4672a8fbee1bca8dd282e2cbf9)) - dependabot[bot]
- bump PurpleBooth/versio-release-action from 0.1.7 to 0.1.8 - ([6dfa6e3](https://github.com/PurpleBooth/generate-formula-action/commit/6dfa6e321eb45573fb6cff6da67b3d91cfb2eed5)) - dependabot[bot]
- bump actions/checkout from 2.4.0 to 3 - ([c9d752c](https://github.com/PurpleBooth/generate-formula-action/commit/c9d752cb4824cf86733ddc369150c10d64756b31)) - dependabot[bot]
- bump PurpleBooth/versio-release-action from 0.1.6 to 0.1.7 - ([8b28155](https://github.com/PurpleBooth/generate-formula-action/commit/8b2815539ee7570e94da7bf4b25abf88ea7b8ef7)) - dependabot[bot]
- bump PurpleBooth/changelog-action from 0.3.0 to 0.3.1 - ([c1ef485](https://github.com/PurpleBooth/generate-formula-action/commit/c1ef485cb93a11ae1a7fb567b3ee85cea381324a)) - dependabot[bot]
- bump ncipollo/release-action from 1.8.10 to 1.9.0 - ([7f17e44](https://github.com/PurpleBooth/generate-formula-action/commit/7f17e44ff182eb338c67302b0a27349fd6c59aaa)) - dependabot[bot]
- bump PurpleBooth/versio-release-action from 0.1.5 to 0.1.6 - ([800000a](https://github.com/PurpleBooth/generate-formula-action/commit/800000a032a9a5b726f0020ee980de3749686aad)) - dependabot[bot]
- bump PurpleBooth/changelog-action from 0.2.2 to 0.3.0 - ([432c5f6](https://github.com/PurpleBooth/generate-formula-action/commit/432c5f6a56eea12fa811ad05230d0272de50faaf)) - dependabot[bot]
- bump PurpleBooth/changelog-action from 0.1.2 to 0.2.2 - ([3fc8543](https://github.com/PurpleBooth/generate-formula-action/commit/3fc854389e86f8ae71bd4fbc8536f199c72a99e0)) - dependabot[bot]
- Correctly generate changelog in the pr - ([2555a15](https://github.com/PurpleBooth/generate-formula-action/commit/2555a15e1240b7045cabbc2e259a3ffd2b646cac)) - Billie Thompson
- bump PurpleBooth/versio-release-action from 0.1.4 to 0.1.5 - ([83a39aa](https://github.com/PurpleBooth/generate-formula-action/commit/83a39aaacee24021ea1919153e95a86f05053ca7)) - dependabot[bot]
- bump actions/checkout from 2.3.5 to 2.4.0 - ([dc8ddc7](https://github.com/PurpleBooth/generate-formula-action/commit/dc8ddc7a5380649a042920c83e5d4e12302da0c0)) - dependabot[bot]
#### Continuous Integration
- **(mergify)** Allow the pending job mergify - ([cb5b174](https://github.com/PurpleBooth/generate-formula-action/commit/cb5b174c5457892e3d4d06a53fdf7bac81b062e5)) - Billie Thompson
- Remove rust related actions from cog - ([667184f](https://github.com/PurpleBooth/generate-formula-action/commit/667184f9bf7d1bf392b0d7eeddfb26c058deca0c)) - Billie Thompson
- Add renovate.json - ([bc01c84](https://github.com/PurpleBooth/generate-formula-action/commit/bc01c84df2b298769d1f56271c7716f9c60b0d57)) - renovate[bot]
- Use cog to bump versions - ([2d00b94](https://github.com/PurpleBooth/generate-formula-action/commit/2d00b94d14dafbbefbfcce67d3b869bffc7a3c4f)) - Billie Thompson
- Switch to cocogitto - ([e5807eb](https://github.com/PurpleBooth/generate-formula-action/commit/e5807ebd380b2d4da63d66ba5113c10e362f3b65)) - Billie Thompson
- Switch to cog - ([3f4ede1](https://github.com/PurpleBooth/generate-formula-action/commit/3f4ede1ea4f1d26a5ceeb06b74099c633f589882)) - Billie Thompson
- Use new output style - ([2d01274](https://github.com/PurpleBooth/generate-formula-action/commit/2d01274fed9ec4c096f4fe201d012738606cfcea)) - Billie Thompson
- Use latest commit check - ([fb009c0](https://github.com/PurpleBooth/generate-formula-action/commit/fb009c02fccfc55387791cf1be6322089827b259)) - Billie Thompson

- - -

Changelog generated by [cocogitto](https://github.com/cocogitto/cocogitto).