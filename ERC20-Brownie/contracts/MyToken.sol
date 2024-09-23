// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;


import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";


contract MyToken is ERC20, Ownable {
    uint256 public constant TOTAL_SUPPLY_LIMIT = 1000000 * (10 ** 18);
    uint256 public totalMinted;

    constructor(address[] memory recipients, address initialOwner) ERC20("MyToken", "MTK") Ownable(initialOwner) {
        mintInitialTokens(recipients);
    }

    function mintInitialTokens(address[] memory recipients) internal {
        uint256 amountPerRecipient = 100000 * (10 ** 18);

        for (uint256 i = 0; i < recipients.length; i++) {
            require(totalMinted + amountPerRecipient <= TOTAL_SUPPLY_LIMIT, "Total supply limit exceeded");
            _mint(recipients[i], amountPerRecipient);
            totalMinted += amountPerRecipient;
        }
    }

    function mint(address to, uint256 amount) external onlyOwner {
        require(totalMinted + amount <= TOTAL_SUPPLY_LIMIT, "Total supply limit exceeded");
        _mint(to, amount);
        totalMinted += amount;
    }

    

}