// swift-tools-version:4.2
import PackageDescription

let package = Package(
    name: "MellonCore",
    products: [
        .library(name: "MellonCore", targets: ["MellonCore"]),
    ],
    dependencies: [
        // 💧 A server-side Swift web framework.
        // .package(url: "https://github.com/vapor/vapor.git", from: "3.0.0"),

        // 🔵 Swift ORM (queries, models, relations, etc) built on SQLite 3.
//        .package(url: "https://github.com/vapor/fluent-sqlite.git", from: "3.0.0"),
//        .package(path: "../MellonSlackModule),
//        .package(path: "../MellonDiscordModule"),
    ],
    targets: [
        .target(name: "MellonCore", dependencies: []),
        .testTarget(name: "MellonCoreTests", dependencies: ["MellonCore"]),
    ]
)
